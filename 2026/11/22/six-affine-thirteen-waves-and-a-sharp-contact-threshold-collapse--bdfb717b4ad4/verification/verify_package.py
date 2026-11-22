"""Independent all-state finite-graph replay and geometric-wave checks."""
import collections
import itertools
import pathlib
import re
import subprocess
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
Q = (1, 3, 4, 9, 10, 12)
N = 13
P = [3**i for i in range(N)]
TOTAL = 3**N

def colors(i):
    return tuple((i // P[j]) % 3 for j in range(N))

def step(x, threshold):
    return tuple(2 if x[i] == 1 else 0 if x[i] == 2
                 else int(sum(x[(i + j) % N] == 1 for j in Q) >= threshold)
                 for i in range(N))

def table_a(raw):
    cycle_str = re.search(r'^ATTRACTORS (.*)$', raw, re.M).group(1)
    cycles = {int(p):int(c) for p,c in re.findall(r'(\d+):(\d+)',cycle_str)}
    depth = int(re.search(r'^MAXENT (\d+)',raw,re.M).group(1))
    hist_str=re.search(r'^JOINT (.*)$',raw,re.M).group(1)
    hist={(int(d),int(p)):int(c) for d,p,c in re.findall(r'\((\d+),(\d+)\)=(\d+)',hist_str)}
    sizes={}
    for p,s in re.findall(r'^BASINPERIOD (\d+) (.*)$',raw,re.M):
        sizes[int(p)]={int(a):int(b) for a,b in re.findall(r'(\d+):(\d+)',s)}
    return cycles,depth,hist,sizes

def table_b(raw,threshold):
    segment=raw.split('threshold '+str(threshold)+' total')[1].split('threshold ',1)[0]
    depth=int(re.search(r'max_depth (\d+)',segment).group(1))
    cycle_str=re.search(r'^cycles(.*)$',segment,re.M).group(1)
    cycles={int(p):int(c) for p,c in re.findall(r'(\d+):(\d+)',cycle_str)}
    hist_str=re.search(r'^histogram(.*)$',segment,re.M).group(1)
    hist={(int(d),int(p)):int(c) for d,p,c in re.findall(r'(\d+),(\d+):(\d+)',hist_str)}
    sizes={}
    for p,s in re.findall(r'^basins (\d+)(.*)$',segment,re.M):
        sizes[int(p)]={int(a):int(b) for a,b in re.findall(r'(\d+):(\d+)',s)}
    return cycles,depth,hist,sizes

def check_geometry():
    w=tuple(int(c) for c in '0000002221110')
    # The three-state excitation map advances the wave by three residues.
    assert step(w,2)==tuple(w[(i-3)%N] for i in range(N))
    waves=set()
    for a,b in itertools.product(Q,range(N)):
        inv=pow(a,-1,N)
        waves.add(tuple(w[((i-b)*inv)%N] for i in range(N)))
    assert len(waves)==78
    seen=set();n_orbits=0
    for x in waves:
        if x in seen: continue
        n_orbits+=1
        orbit=[];y=x
        while y not in seen:
            assert y in waves
            seen.add(y);orbit.append(y);y=step(y,2)
        assert y==x and len(orbit)==13
    assert n_orbits==6 and len(seen)==78
    # Every affine multiplier sends the translating wave to another translating wave.
    for x in waves:
        speeds=[d for d in Q if step(x,2)==tuple(x[(i-d)%N] for i in range(N))]
        assert len(speeds)==1
    return len(waves),n_orbits

with tempfile.TemporaryDirectory(prefix='excitation_replay_') as td:
    programs={}
    for name in ('census_detail','paley13_peel'):
        executable=pathlib.Path(td)/name
        subprocess.run(['g++','-O2','-std=c++17',str(ROOT/"verification"/(name+'.cpp')),'-o',str(executable)],check=True)
        programs[name]=executable
    b=subprocess.run([str(programs['paley13_peel'])],capture_output=True,text=True,check=True).stdout
    for threshold in (2,3):
        graph=ROOT/"graph"/f'paley13_t{threshold}.txt'
        lines=graph.read_text().splitlines()
        assert lines[0]==f'paley13 13 {threshold}'
        for i,line in enumerate(lines[1:]):
            values=[int(v) for v in line.split()]
            assert values==[6]+sorted((i+d)%N for d in Q)
        a=subprocess.run([str(programs['census_detail'])],input=graph.read_text(),capture_output=True,text=True,check=True).stdout
        u=table_a(a)
        v=table_b(b,threshold)
        assert u==v,('exhaustive algorithms disagree',threshold)
        cycles,depth,hist,sizes=u
        assert sum(hist.values())==TOTAL
        assert sum(p*c for p,c in cycles.items())==sum(c for (t,p),c in hist.items() if t==0)
        assert max(t for t,p in hist)==depth
        assert sum(cnt for size,cnt in sizes.get(13,{}).items())==cycles.get(13,0)
        if threshold==2:
            assert cycles=={1:1,3:2288,13:6} and depth==14
            assert sizes[13]=={1235:6}
            assert sum(c for (_,p),c in hist.items() if p==1)==1498799
            assert sum(c for (_,p),c in hist.items() if p==3)==88114
            assert sum(c for (_,p),c in hist.items() if p==13)==7410
            assert hist[(14,1)]==624
        else:
            assert cycles=={1:1} and depth==4
            assert hist[(4,1)]==101062
        print(f'threshold={threshold}: states={TOTAL} attractors={cycles} maximum_entry={depth} full_joint_and_basin_tables_agree=yes')
    wave_states,wave_orbits=check_geometry()
    print(f'geometric affine orbit={wave_states} periodic states, {wave_orbits} primitive period-13 orbits; all waves verified')
print('PASS: two distinct full-state algorithms, exact graph specification, period-13 geometry')
