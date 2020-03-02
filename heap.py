def generate(A):
  c = [0] * len(A)
  print(A)
  
  i = 0
  while i < len(A):
    if c[i] < i:
      if i % 2:
        A[c[i]], A[i] = A[i], A[c[i]]
      else:
        A[0], A[i] = A[i], A[0]
      
      print(A)
      c[i] = c[i] + 1
      i = 0
    else:
      c[i] = 0
      i = i + 1

generate([1,2,3,4])