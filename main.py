from carrot import get_jobs
from save_to_csv import save_to_csv

res = get_jobs()
save_to_csv(res)
print(res)