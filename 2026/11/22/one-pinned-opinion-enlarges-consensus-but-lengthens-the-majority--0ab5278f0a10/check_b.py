"""Alternative exhaustive state enumerator for majority on the four-cube.

Bit zero is the fixed-one vertex in the clamped variant.  All states are
explicitly iterated; path following, rather than indegree pruning, assigns
first-entry times and eventual primitive periods.
"""
from collections import Counter, defaultdict
from itertools import product

vertices = tuple(tuple(v ^ (1 << bit) for bit in range(4)) for v in range(16))

def update(word, clamp):
    colors = [(word >> v) & 1 for v in range(16)]
    output = [0] * 16
    for v in range(16):
        if v == 0 and clamp:
            output[v] = 1
            continue
        yes = sum(colors[w] for w in vertices[v])
        output[v] = (1 if yes >= 3 else 0 if yes <= 1 else colors[v])
    return sum(bit * (1 << v) for v, bit in enumerate(output))

def classify(clamp):
    labels = list(range(1,1 << 16,2)) if clamp else list(range(1 << 16))
    index = {label: i for i, label in enumerate(labels)}
    successors = [index[update(state, clamp)] for state in labels]
    n=len(labels)
    durations=[-1] * n
    periods=[0] * n
    orbit_of=[-1] * n
    cycles=[]
    for root in range(n):
        if durations[root] >= 0:
            continue
        path=[];position={};current=root
        while durations[current] < 0 and current not in position:
            position[current] = len(path)
            path.append(current)
            current=successors[current]
        if durations[current] < 0:
            j=position[current]
            members=path[j:]
            period=len(members)
            k=len(cycles)
            cycles.append(members)
            for member in members:
                durations[member]=0
                periods[member]=period
                orbit_of[member]=k
            path=path[:j]
        for member in reversed(path):
            successor=successors[member]
            durations[member]=durations[successor]+1
            periods[member]=periods[successor]
            orbit_of[member]=orbit_of[successor]
    sizes=Counter(orbit_of)
    return labels, successors, durations, periods, cycles, orbit_of, sizes

cl=classify(True)
un=classify(False)
labels,nexts,depth,periods,cycles,orbit,sizes=cl
ulabels,_,udepth,uperiods,ucycles,uorbit,usizes=un
cnum=next(i for i,cycle in enumerate(cycles) if len(cycle)==1 and labels[cycle[0]]==65535)
lonenum=next(i for i,cycle in enumerate(cycles) if len(cycle)==1 and labels[cycle[0]]==1)
ucnum=next(i for i,cycle in enumerate(ucycles) if len(cycle)==1 and ulabels[cycle[0]]==65535)
gained=0;lost=0;baseyes=0;pinyes=0
for i,word in enumerate(labels):
    pinned = orbit[i] == cnum
    baseline = uorbit[word] == ucnum
    gained += int(pinned and not baseline)
    lost += int(baseline and not pinned)
    pinyes += int(pinned)
    baseyes += int(baseline)
print('secondary: cycles=',dict(sorted(Counter(map(len,cycles)).items())))
print('secondary: time_by_period=',sorted(Counter(zip(depth,periods)).items()))
print('secondary: clamped consensus=',sizes[cnum], 'single_seed=',sizes[lonenum])
print('secondary: baseline_cycles=',dict(sorted(Counter(map(len,ucycles)).items())),'baseline_depth=',max(udepth))
print('secondary: matched_initial_1=',baseyes,pinyes, 'gains=',gained,'losses=',lost)
print('secondary: sharp_last_layer=',sum(t==6 for t in depth))
assert (len(cycles),max(depth),sizes[cnum],sizes[lonenum])==(726,6,9383,3696)
assert (baseyes,pinyes,gained,lost)==(8229,9383,1154,0)
assert Counter(map(len,cycles))=={1:425,2:301}
assert Counter(zip(depth,periods))=={(0,1):425,(0,2):602,(1,1):5490,(1,2):3187,(2,1):12713,(2,2):3562,(3,1):5171,(3,2):172,(4,1):1224,(5,1):198,(6,1):24}
assert all(len(c)<=2 for c in cycles)
assert Counter(map(len,ucycles))=={1:702,2:885}
assert max(udepth)==4
# Direct independent witness evaluation
path=[35537]
for _ in range(6): path.append(update(path[-1],True))
assert path==[35537,35025,32977,209,81,17,1]
assert update(1,True)==1
print('secondary: witness=',path)
