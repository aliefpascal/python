# create zero matrix with rnum rows and cnum columns
def zero(rnum, cnum):
  m = []
  for r in range(rnum):
    r = []
    for c in range(cnum):
      c = 0
      r.append(c)
    m.append(r)
  return m


# get string representation of matrix
def mat2str(m, fmt=".2e"):
  mstr = ""
  rnum = len(m)
  cnum = len(m[0])
  for r in range(rnum):
    rstr = ""
    for c in range(cnum):
      cstr = f"{m[r][c]:{fmt}}"
      rstr += cstr
      rstr += " "
    rstr += "\n"
    mstr += rstr
  return mstr


# stack rows of two matrices 
def stackrows(x, y):
  z = x + y
  return z


# stack columns of two matrices 
def stackcols(x, y):
  rnum = len(x)
  cnum = len(y[0])
  z = x.copy()
  for r in range(rnum):
    for c in range(cnum):
      z[r].append(y[r][c])
  return z


# addition of two matrices 
def add(x, y):
  rnum = min(len(x), len(y))
  cnum = min(len(x[0]), len(y[0]))
  z = zero(rnum, cnum)
  for i in range(rnum):
    for j in range(cnum):
      z[i][j] = x[i][j] + y[i][j]
  return z

# substraction of two matrices 
def sub(x, y):
  rnum = min(len(x), len(y))
  cnum = min(len(x[0]), len(y[0]))
  z = zero(rnum, cnum)
  for i in range(rnum):
    for j in range(cnum):
      z[i][j] = x[i][j] - y[i][j]
  return z
