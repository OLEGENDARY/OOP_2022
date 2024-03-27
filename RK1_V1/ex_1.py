import random


def initialize_rand_list(n):
  list = []
  while len(list) < n:
    rand = random.randint(-40, 40)
    if rand not in list:
      list.append(rand)
  return sorted(list)


def found_nums(list, k):
  new_list = []
  for i in range(len(list)):
    for j in range(i + 1, len(list) - 1):
      if list[i] + list[j] == k:
        new_list.append(list[i])
        new_list.append(list[j])
      
  if len(new_list) == 0:
    return -1
  elif len(new_list) > 0:
    return new_list


if __name__ == "__main__":
  cntr = 0
  while True:
    list = []
    list = initialize_rand_list(random.randint(1, 20))
    print(f"length = {len(list)}", list, sep="\n")

    k = random.randint(-10, 10)
    print(f"k = {k}", found_nums(list, k), sep="\n", end="\n\n")

    if found_nums(list, k) == -1:
      cntr += 1
    elif  found_nums(list, k) != -1:
      break

  print(f"количество неудачных попыток: {cntr}")
