def uncollapse(s):
  nums = ['zero', 'one', 'two', 'three', 'four',
          'five', 'six', 'seven', 'eight', 'nine']
  for num in nums:
    s = s.replace(num,'{} '.format(num))
  return s.strip()
