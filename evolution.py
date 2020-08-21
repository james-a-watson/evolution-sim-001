import creatures as ctr
import analysis as anl
import pandas as pd


def generation(group, days):
    gen1_post_hunt = ctr.feeding(group, days)
    data1 = anl.group_data(gen1_post_hunt)
    analysis1 = anl.analyse_group(data1)

    gen2 = ctr.mating(gen1_post_hunt)

    return gen2, analysis1


def multi_run(group_size, group_nature, days, generations):
    gen = [ctr.original_gen(group_size, group_nature)]
    analysis = pd.DataFrame(columns=[
                            'Selfish', 'Sharing', 'Males', 'Females', 'Survivors', 'Avg Max Health', 'Avg Health', 'Avg Speed'])
    for x in range(generations):
        gen = generation(gen[0], days)
        analysis = analysis.append(gen[1])

    return analysis


multi_run(50, 'selfish', 50, 100).to_excel('test1.xlsx')
