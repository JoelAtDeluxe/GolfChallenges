# Rules:
# 1T = 4W + 3D
# CMD ordering: #W #D #A
import math

def determine_turkeys(num_white, num_dark, num_any):
  min_turkeys = math.ceil(max(num_white / 4, num_dark / 3))
  leftover_servings = (min_turkeys * 7) - num_white - num_dark
  needs = num_any - leftover_servings
  extras = 0 if needs <= 0 else math.ceil(needs/7)
  result = int(min_turkeys + extras)
  return result

def cook_turkeys(num):
  return '\n'.join(['      .---.   _   ' * num,
                    "    .'     './ )  " * num,
                    '   /   _   _/ /\  ' * num,
                    ' =(_____) (__/_/==' * num,
                    '==================' * num]) + '='

if __name__ == '__main__':
  # print(cook_turkeys(determine_turkeys(0, 20, 0)))
  print(determine_turkeys(5, 4, 10))