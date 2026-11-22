from functools import lru_cache
from itertools import product

def is_cold_by_boundary(w):
    if not w:return True
    s=0;heights=[0]
    for c in w:
        s+=(1 if c=='a' else -1)
        heights.append(s)
    h=heights[-1]
    if h==0:return False
    e=['A' if t==0 else 'B' for t in heights if t==0 or t==h]
    if e[0]!='A' or e[-1]!='B':raise AssertionError(w)
    z=e[1:-1]
    s=0
    for c in z:
        s+=(1 if c=='A' else -1)
        if s<0:return False
    return s==0

@lru_cache(None)
def game(w):
    pre=[0];s=0
    for c in w:
        s+=1 if c=='a' else -1
        pre.append(s)
    moves={game(w[t:]) for t in range(1,len(w)+1) if pre[t]==0}
    moves.update(game(w[:t]) for t in range(len(w)) if pre[t]==s)
    return next(v for v in range(len(moves)+1) if v not in moves)

for n in range(17):
    for letters in product('ab',repeat=n):
        w=''.join(letters)
        assert (game(w)==0)==is_cold_by_boundary(w),(w,game(w))
for i in range(1,15):
    for j in range(1,15):
        w='b'*i+'a'*j+'b'
        assert is_cold_by_boundary(w)==(j>=i+2),(i,j)
print('BOUNDARY_GAME_OK lengths=0..16')
print('NONREGULAR_SLICE_OK i,j=1..14')
