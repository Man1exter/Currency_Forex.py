def Bin_Search(tab[], x, left, right):             T(n)
    
  if(left = rigth-1):                              0(1)

    return 0                                       0(1)

  mid = (left+rigth)//2                            0(1)
 
  if(tab[mid] = x):                                0(1)

    return mid                                     0(1)

  if(tab[mid] > x:                                 0(1)

    return Bin_Search(tab[], x, left, mid)         T(n/2)

  else:                                            0(1)

    return Bin_Search(tab[], x, mid, right)        T(n/2)


T(n) = T(1/2)
T(n) = 0(f(n))