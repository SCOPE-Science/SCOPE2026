from collections import Counter
from itertools import product
from math import comb

def update(state,m):
    h,kh=state[:2]
    leaves=[state[2+2*i:4+2*i] for i in range(m)]
    next_h=int(h+sum(x for x,k in leaves)>=kh)
    out=[next_h,kh+next_h-h]
    for x,k in leaves:
        y=int(x+h>=k)
        out.extend((y,k+y-x))
    return tuple(out)

def explore(m):
    depth=Counter(); eventual=Counter(); orbit_size=Counter(); cycle_basins=Counter()
    orbit_types={}
    for hub in product((0,1),range(1,m+2)):
        for leaves in product(((0,1),(0,2),(1,1),(1,2)),repeat=m):
            s=hub+tuple(z for pair in leaves for z in pair)
            seen={}; trajectory=[];u=s
            while u not in seen:
                seen[u]=len(trajectory);trajectory.append(u);u=update(u,m)
                assert len(trajectory)<=5
            t=seen[u];period=len(trajectory)-t
            cyc=tuple(trajectory[t:]); key=min(cyc)
            depth[t]+=1; eventual[period]+=1
            cycle_basins[key]+=1
            orbit_types[key]=period
    for key,p in orbit_types.items():orbit_size[p]+=1
    observed=Counter(cycle_basins[key] for key,p in orbit_types.items() if p==2)
    expected=Counter({2**c:comb(m,c)*2**(m-c)*c for c in range(1,m+1)})
    assert observed==expected,(m,observed,expected)
    total=2*(m+1)*4**m
    immediate_fixed=2*(2*m+3)*3**(m-1)
    cycles=m*3**(m-1)
    oscill_basin=2*m*4**(m-1)
    depth2=m*(2*4**(m-1)-2**m)
    assert sum(depth.values())==total
    assert orbit_size[1]==immediate_fixed and orbit_size[2]==cycles
    assert eventual[2]==oscill_basin and depth[2]==depth2
    assert depth[0]==immediate_fixed+2*cycles
    assert depth[1]==total-depth[0]-depth[2]
    print('m=',m,'states=',total,'fixed=',immediate_fixed,'primitive_two_orbits=',cycles,'osc_basin=',oscill_basin,'entrance=',dict(sorted(depth.items())),'two_cycle_basin_size_spectrum=',dict(sorted(observed.items())),flush=True)

if __name__=='__main__':
    for m in range(1,7):explore(m)
    print('PASS all extended states and individual two-cycle orbit basins for m=1..6')
