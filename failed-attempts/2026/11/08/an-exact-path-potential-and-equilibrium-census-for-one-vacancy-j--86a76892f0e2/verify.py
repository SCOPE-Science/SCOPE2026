#!/usr/bin/env python3
"""Exact finite checks for one-vacancy two-colour jump dynamics on bicliques.

Checks a theorem about type-homogeneous utilities of closed-neighbourhood
same-type shares. Finite checking corroborates but does not replace the proof.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import comb, factorial


def score(z, peak):
    return z / peak if z <= peak else (1 - z) / (1 - peak)


def interval_states(a, b, red):
    out = {}
    for x in range(a):
        if 0 <= red - x <= b:
            out[2*x] = ('A', x)
    for x in range(a+1):
        if 0 <= red - x <= b-1:
            out[2*x-1] = ('B', x)
    assert out
    assert set(out) == set(range(min(out), max(out)+1))
    return out


def arrow_table(a, b, red, peak_r, peak_b):
    states = interval_states(a, b, red)
    arrows = {}
    for t in range(min(states), max(states)):
        # directed edge: t -> t+1; t odd => B_x -> A_x (blue),
        # t even => A_x -> B_{x+1} (red)
        if t % 2:
            x = (t+1)//2
            gain = score(Q(a-x,a),peak_b) - score(Q(b-red+x,b),peak_b)
        else:
            x = t//2
            gain = score(Q(red-x,b),peak_r) - score(Q(x+1,a),peak_r)
        arrows[t] = (gain > 0) - (gain < 0)
    phi={min(states):0}
    for t in range(min(states),max(states)):
        phi[t+1]=phi[t]+arrows[t]
    return states,arrows,phi


def potential_fraction(state, index, a, peak_r, peak_b):
    colour = state[index]
    assert colour != -1
    n=len(state)
    opposite = range(a,n) if index < a else range(0,a)
    neigh = [state[j] for j in opposite if state[j] != -1]
    f = Q(1+sum(z==colour for z in neigh),1+len(neigh))
    return score(f,peak_r if colour==1 else peak_b)


def projection(state,a):
    vacant=state.index(-1)
    x=sum(state[i]==1 for i in range(a))
    return 2*x if vacant<a else 2*x-1


def run():
    states_count=edges_count=move_checks=stable_checks=instances=0
    test_peaks=[(Q(1,4),Q(1,4)),(Q(2,5),Q(2,5)),
                (Q(1,2),Q(1,2)),(Q(3,5),Q(3,5)),
                (Q(3,4),Q(3,4)),(Q(1,3),Q(2,3))]
    for a in range(1,6):
      for b in range(1,6):
        n=a+b
        if n<3:continue
        for red in range(1,n-1):
          blue=n-1-red
          for peak_r,peak_b in test_peaks:
            instances+=1
            S,arrows,phi=arrow_table(a,b,red,peak_r,peak_b)
            states_count+=len(S)
            edges_count+=len(arrows)
            assert len(S)-1<=2*min(a,b)
            stable_pred={t for t in S if all(phi[t]>=phi[t2] for t2 in [t-1,t+1] if t2 in S)}
            assert stable_pred
            predicted_configs=0
            for t,(vacant_part,x) in S.items():
                if t not in stable_pred: continue
                if vacant_part=='A':
                    ways=a*comb(a-1,x)*comb(b,red-x)
                else:
                    ways=b*comb(a,x)*comb(b-1,red-x)
                predicted_configs+=ways
            observed_configs=0
            proj_freq={t:0 for t in S}
            for vacant in range(n):
              positions=[i for i in range(n) if i!=vacant]
              for reds in combinations(positions,red):
                R=set(reds)
                state=tuple(-1 if i==vacant else (1 if i in R else 0) for i in range(n))
                t=projection(state,a)
                assert t in S
                proj_freq[t]+=1
                stable=True
                for i in positions:
                  new=list(state)
                  new[vacant]=state[i]
                  new[i]=-1
                  new=tuple(new)
                  gain=potential_fraction(new,vacant,a,peak_r,peak_b)-potential_fraction(state,i,a,peak_r,peak_b)
                  move_checks+=1
                  t2=projection(new,a)
                  if (i<a)==(vacant<a):
                    assert gain==0 and t2==t
                  else:
                    assert abs(t2-t)==1
                    sign=arrows[min(t,t2)]
                    exp_sign=sign if t2>t else -sign
                    assert (gain>0)-(gain<0)==exp_sign
                    if gain>0:
                      stable=False
                      assert phi[t2]==phi[t]+1
                if stable:
                   observed_configs+=1
                   assert t in stable_pred
                else:
                   assert t not in stable_pred
            assert observed_configs==predicted_configs
            stable_checks+=observed_configs
            for t,(side,x) in S.items():
               expected=(a*comb(a-1,x)*comb(b,red-x) if side=='A'
                         else b*comb(a,x)*comb(b-1,red-x))
               assert proj_freq[t]==expected
    print('PASS: instances=',instances,'projected_states=',states_count,
          'edges=',edges_count,'direct_move_checks=',move_checks,
          'stable_colour_configurations=',stable_checks)
    print('The general proof, not the finite experiments, certifies all graph sizes and utility functions.')

if __name__=='__main__': run()
