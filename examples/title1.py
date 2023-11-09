import matplotlib.pyplot as plt
from mpl_ornaments.titles import set_title_and_subtitle

#Create an empty figure with one subplot
fig, ax = plt.subplots(figsize=(5,6))

#Add title and subtitle
set_title_and_subtitle(fig=fig, title='Figure title', 
                       subtitle='Figure subtitle')

#Save the figure
fig.savefig(fname='title1.png')
