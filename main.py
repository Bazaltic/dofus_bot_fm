from classes.line import load_settings
from classes.data import *
from ui.interface import *
import time

"""USE_RUNE_PA = False
USE_RUNE_RA = False
RUNE_TO_COMPUTE = 20

start_time = time.time()
settings = load_settings()

stats = settings["stats"]
button_fusion = settings["button_fusion"]
print("Load settings : {} seconds".format(int(time.time() - start_time)))
start_time = time.time()

item = ItemInfo(stats, 7, 1)
print("Prepare object : {} seconds".format(int(time.time() - start_time)))

for i in range(RUNE_TO_COMPUTE):
    start_time = time.time()
    item.compute_info()
    line = item.get_best_stat_to_fm()
    line.apply_rune(USE_RUNE_PA, USE_RUNE_RA)
    print("Rune {}/{} : {} seconds".format(i+1, RUNE_TO_COMPUTE, int(time.time() - start_time)))"""

launch()