"""Independent brute-force vertex-level check, deliberately without transfer matrices."""

def update(state, adjacency):
    out=0
    for i,neighbors in enumerate(adjacency):
        alive=sum((state>>j)&1 for j in neighbors)
        deg=len(neighbors)
        nxt=1 if 2*alive>deg else (0 if 2*alive<deg else ((state>>i)&1))
        out|=nxt<<i
    return out

def compute(n,deleted):
    adj=[]
    for i in range(n):
        adj.append([j for j in range(n) if min((i-j)%n,(j-i)%n) in (1,2) and frozenset((i,j))!=frozenset((0,deleted))])
    f=p=0
    for state in range(1<<n):
        nextstate=update(state,adj)
        if nextstate==state:f+=1
        elif update(nextstate,adj)==state:p+=1
    return f,p//2

if __name__=='__main__':
    total=0
    for n in range(7,17):
        for d in (1,2):
            f,c=compute(n,d)
            want=2*(n%4==0)+2*(n%6==0)+(d==2 and n%4==3)
            assert c==want,(n,d,f,c,want)
            print('n',n,'distance',d,'fixed',f,'primitive_2_orbits',c)
            total+=(1<<n)
    print('INDEPENDENT_DIRECT_CHECK_OK configurations=',total)
