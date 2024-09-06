import pandas as pd
import numpy as np
from bokeh.models.tools import HoverTool
from bokeh.models import ColumnDataSource, CustomJSTickFormatter, CheckboxGroup, Select, RangeSlider
from bokeh.models.widgets import TableColumn, DataTable
from bokeh.models.layouts import TabPanel
from bokeh.palettes import Category20_16
from bokeh.plotting import figure
from bokeh.layouts import column, row

def lig_graf(data):
    # Function to extract and create data and draw graphs.
    def Numplyaer_age(data):
        # making data
        def md(s_data, rs=15, re=41, bin=1):
            d = pd.DataFrame(columns=['proportion', 'left', 'right', 'f_proportion', 'f_interval', 'Comp', 'color'])
            r = re - rs
            for i, r_data in enumerate(s_data):
                subset = data[data['Comp'] == r_data]
                arr_hist, edge = np.histogram(subset['Age'], bins=int(r / bin), range=(rs, re))
                arr_df = pd.DataFrame({
                    'proportion' : arr_hist,
                    'left': edge[:-1],
                    'right' : edge[1:]
                })
                arr_df['f_proportion'] = ['%0.5f' % p for p in arr_df['proportion']]
                arr_df['f_interval'] = ['%d to %d minutes' % (left, right) for left, right in zip(arr_df['left'], arr_df['right'])]
                arr_df['Comp'] = r_data
                arr_df['color'] = Category20_16[i]
                d = pd.concat([d, arr_df], ignore_index = True)
            d = d.sort_values(['Comp', 'left'])
            d = ColumnDataSource(d)
            return d
        
        # making plot
        def mp(s_data):
            p = figure(title='number', height=399, width=600)
            p.quad(
                source=s_data, bottom=0, top='proportion', left='left', right='right', color='color', fill_alpha=0.7, legend_field='Comp'
                )
            p.xaxis.axis_label = 'Age'
            return p
        
        # update function
        def update(attr, old, new):
            comp_check = [chbox.labels[i] for i in chbox.active]
            ds = md(comp_check, renge_slider.value[0], renge_slider.value[1])
            src.data.update(ds.data)
        
        comp = list(set(data['Comp']))
        comp.sort()

        chbox = CheckboxGroup(labels=comp, active=[0, 1])
        chbox.on_change('active', update)

        renge_slider = RangeSlider(start=15, end=41, value=(15, 41), step=1, title='Age range')
        renge_slider.on_change('value', update)

        init_data = [chbox.labels[i] for i in chbox.active]

        src = md(init_data)
        p = mp(src)
        w = column(chbox, renge_slider, width=170)
        r = row(w, p, )
        return r
    
    
    def Country_player(data):

        def md(comp, country):
            xs = []
            ys = []
            dic = {'0' : country}
            subset = data[(data['Comp'] == comp) & (data['Nation'] == country)]
            subset['x'] = list(range(1, len(subset) + 1))
            subset['y'] = 0
            return ColumnDataSource(data=subset), dic

        def mp(src, comp_inits, coutry_inits, dic):
            p = figure(width=600, height=399, title='country')
            p.scatter('x', 'y', source=src, size=20)
            p.yaxis[0].ticker.desired_num_ticks = len(dic)
            p.yaxis.formatter = CustomJSTickFormatter(
                code="""
                var labels = %s
                return labels[tick];
                """ % dic
            )
            p.xaxis.axis_label= 'Number Of Player'
            h = HoverTool()
            h.tooltips = [
            ('Name', '@Player'),
            ('Age', '@Age'),
            ('Squad', '@Squad'),
            ('Minutes played', '@Min'),
            ('Position', '@Pos'),
            ('Goals scored ', '@Goals'),
            ('Assists', '@Assists'),
            ('Yellow cards', '@CrdY'),
            ('Red cards', '@CrdR')
            ]
            p.add_tools(h)
            return p
        
        def update(attr, old, new):
            comp = comp_s.value
            country = country_s.value
            new_src, new_dic = md(comp, country)
            src.data.update(new_src.data)
            p.yaxis.formatter = CustomJSTickFormatter(
                code="""
                var labels = %s
                return labels[tick];
                """ % new_dic
            )

        comp = list(set(data['Comp']))
    
        country = list(set(data['Nation']))
        country = [x for x in country if isinstance(x, str) and pd.notna(x)]

        comp_s = Select(title='League', value='Premier League', options=comp)
        country_s = Select(title='Countries ', value='ENG', options=country)

        comp_s.on_change('value', update)
        country_s.on_change('value', update)

        comp_init= comp_s.value
        country_init= country_s.value

        src, dic= md(comp_init, country_init)
        p = mp(src, comp_init, country_init, dic)
        w = column(comp_s, country_s, width=120)
        r = row(w, p)
        return r

    def lig_tabel(data):
        d = data.groupby('Comp')[['Goals', 'PasTotCmp', 'CrdY', 'CrdR', 'Off','Fls', 'OG']].sum().round(1)
        age_mean = data.groupby('Comp')['Age'].mean().round(1)
        d['Age'] = age_mean
        d_count = data.groupby('Comp').describe()
        d['count'] = d_count['Rk']['count']
        c = ColumnDataSource(d)
        comp_table = DataTable(
            source=c,
            columns=[
                TableColumn(field='Comp', title='League'),
                TableColumn(field='count', title='Number of players'),
                TableColumn(field='Goals', title='The number of goals'),
                TableColumn(field='PasTotCmp', title='Passes completed per 90 min'),
                TableColumn(field='CrdY', title='Total number of yellow cards per 90 min'),
                TableColumn(field='CrdR', title='Total number of red cards per 90 min'),
                TableColumn(field='Off', title='Total number of offside per 90 min'),
                TableColumn(field='Fls', title='Total number of fouls per 90 min'),
                TableColumn(field='OG', title='Total number of own goals'),
                TableColumn(field='Age', title='Average age'),
            ],
            height=252,
            width=1430,
        )
        return comp_table
    
    tabel_lig = lig_tabel(data)
    graf_lig_age = Numplyaer_age(data)
    graf_lig_nation = Country_player(data)
    r = row(children=[graf_lig_age, graf_lig_nation])
    c = column(children=[tabel_lig, r])
    tab = TabPanel(child=c, title='League')
    return tab



