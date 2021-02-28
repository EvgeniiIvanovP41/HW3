import psutil
import time
import numpy as np
from tqdm import tqdm

count = 0
mass = []

print("\nВас приветствует программа для сбора и анализа используемой опперативной памяти")
print("Автор: Иванов Евгений\n\n")
print("Идет сбор данных (это займет примерно пол минуты):")
for i in tqdm(range(300)):
    data = psutil.virtual_memory()._asdict()
    mass.append(data["used"])
    count += 1
    time.sleep(0.1)
print("ДАННЫЕ УСПЕШНО СОБРАННЫ\n")
print("Результат собранных данных:")
print("  1)Всего данных собрано:", count)
print("  2)перцентиль 50%:", np.percentile(mass, 50))
print("  3)перцентиль 10%:", np.percentile(mass, 10))
print("  4)перцентиль 90%:", np.percentile(mass, 90))
