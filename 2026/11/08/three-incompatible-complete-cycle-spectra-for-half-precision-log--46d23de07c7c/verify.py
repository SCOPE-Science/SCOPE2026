#!/usr/bin/env python3
"""Exact-arithmetic enumeration of three evaluation strategies for the logistic map.
This is a standalone finite mathematical certificate, using only Python stdlib.
"""
from bisect import bisect_left
from collections import Counter
import hashlib
S=1<<24

def scaled_value(bits):
    # positive finite binary16 only, interpreted as integer multiples of 2^-24
    e=(bits>>10)&31; f=bits&1023
    if e==0:return f
    if e==31:raise ValueError('nonfinite')
    return (1024+f) << (e-1)

# For x<=4 all bits 0..0x4400 (including 0, 1 and 4)
CODES=tuple(range(0x4401))
UNITS=tuple(scaled_value(b) for b in CODES)
assert all(a<b for a,b in zip(UNITS,UNITS[1:])); assert UNITS[0]==0 and UNITS[0x3c00]==S and UNITS[0x4400]==4*S

def rnd(num,den=1):
    """Correctly round nonnegative num/den in 2^-24 units to binary16 (nearest even)."""
    assert 0<=num<=4*S*den
    low=bisect_left(UNITS,num//den)
    # Find the first representable unit >= exact rational
    while low<len(UNITS) and UNITS[low]*den<num:low+=1
    if low==0:return 0
    if low==len(UNITS):return len(UNITS)-1
    gaplo=num-UNITS[low-1]*den
    gaphi=UNITS[low]*den-num
    if gaplo<gaphi:return low-1
    if gaplo>gaphi:return low
    # Nearest-even: bit 0 of exponent+fraction field is low significand bit
    return low-1 if ((low-1)&1)==0 else low

def nextbit(b,mode):
    x=UNITS[b]
    if mode=='factored':
        a=rnd(4*x)
        c=rnd(S-x)
        y=rnd(UNITS[a]*UNITS[c],S)
    elif mode=='expanded':
        a=rnd(4*x)
        xx=rnd(x*x,S)
        sq=rnd(4*UNITS[xx])
        y=rnd(UNITS[a]-UNITS[sq])
    elif mode=='once':
        y=rnd(4*x*(S-x),S)
    else:raise ValueError(mode)
    if not 0<=y<=0x3c00:raise AssertionError((b,mode,y))
    return y

def graph(mode):
    f=[nextbit(i,mode) for i in range(0x3c01)]
    state={};cycles=[]
    for start in range(len(f)):
        if start in state:continue
        path=[];local={};j=start
        while j not in state and j not in local:
            local[j]=len(path);path.append(j);j=f[j]
        if j in local:
            c=path[local[j]:]
            cid=len(cycles)
            cycles.append(c)
            for k in c:state[k]=(cid,0)
        for k in reversed(path):
            if k not in state:
                cid,d=state[f[k]];state[k]=(cid,d+1)
    assert len(state)==len(f)
    dct={}
    for i,c in enumerate(cycles):
        dct[str(len(c)) + ':' + str(min(c))]={
            'period':len(c), 'minimal_binary16_bits':f'0x{min(c):04x}',
            'points':len(c),
            'basin_size':sum(x[0]==i for x in state.values()),
            'max_entry_time':max(d for ci,d in state.values() if ci==i),
            'total_entry_time':sum(d for ci,d in state.values() if ci==i),
            'cycle_encoding':c,
        }
    return f,state,sorted(dct.values(),key=lambda z:(z['period'],z['minimal_binary16_bits']))

def main():
    out={}
    for mode in ('factored','expanded','once'):
        f,state,cycles=graph(mode)
        out[mode]={'cycles':cycles,'max_entry_time':max(d for ci,d in state.values()),
                    'sum_entry_time':sum(d for ci,d in state.values()),
                    'edge_vector_sha256':hashlib.sha256(b''.join(int(x).to_bytes(2,'little') for x in f)).hexdigest()}
        assert sum(a['basin_size'] for a in cycles)==15361
        assert len(set(a['minimal_binary16_bits'] for a in cycles))==len(cycles)
        print(mode, [(z['period'],z['basin_size'],z['minimal_binary16_bits']) for z in cycles], 'max',out[mode]['max_entry_time'], 'mean_num',out[mode]['sum_entry_time'])
    assert [z['period'] for z in out['factored']['cycles']]==[1,1,40]
    assert [z['period'] for z in out['expanded']['cycles']]==[1,1,4,17,25,30]
    assert [z['period'] for z in out['once']['cycles']]==[1,1,5]
    expected={
      'factored':([1,1,40],[5092,2,10267],83,389795,'300ed95c25d2fe4a9b836b60802d0c6b8af3c9c1c01e0654f895781ea889027c'),
      'expanded':([1,1,4,17,25,30],[6671,33,91,881,3648,4037],59,242447,'7dac595f8435d93aa3bea32a701ef4c9d19d30f0079195a63f5db7ca0353729c'),
      'once':([1,1,5],[15236,8,117],109,712352,'262e0316d1e5e82c3b1c694ecde3dde9b8c6a8a24956d407f6b6b008c2d116af')
    }
    for mode,(periods,basins,maxdist,sumdist,edgehash) in expected.items():
        assert [z['period'] for z in out[mode]['cycles']]==periods
        assert [z['basin_size'] for z in out[mode]['cycles']]==basins
        assert out[mode]['max_entry_time']==maxdist
        assert out[mode]['sum_entry_time']==sumdist
        assert out[mode]['edge_vector_sha256']==edgehash
    print('EXACT_GRAPH_CHECK_OK')
if __name__=='__main__':main()
