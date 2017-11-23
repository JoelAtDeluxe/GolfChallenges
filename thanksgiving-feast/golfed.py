
# Note: -(-n//d) == math.ceil(n/d)

def determine_turkeys(w, d, a):
  m=max(-(w//-4),-(d//-3))
  e=-(max(0,a+w+d-m*7)//-7)
  s=m+e
  return s

def cook_turkeys(num):
  return '\n'.join(map(lambda x: x*num, ['      .---.   _   ',"    .'     './ )  ",'   /   _   _/ /\  ',' =(_____) (__/_/==','=================='])) + '=' 

def G(w, d, a):
 m=max(-(w//-4),-(d//-3))
 e=-(max(0,a+w+d-m*7)//-7)
 return '\n'.join(map(lambda x: x*(m+e), ['      .---.   _   ',"    .'     './ )  ",'   /   _   _/ /\  ',' =(_____) (__/_/==','='])) + '='*18

if __name__ == '__main__':
  print(G(3, 6, 3))
  
  # print(determine_turkeys(5, 4, 10))