#!/usr/bin/env python3
"""Recompute orbit cells, elementary collapses and presentation eliminations.

All simplices are re-enumerated from the stable-pair definitions. No stored
precomputed boundary matrices or external libraries are used.
"""
import collections
import contextlib
import io
from orbit_presentation import pi1


def verify():
    expected = {
      (8,'cyclic'): (1105,517,(12,35,24),23,[[9,9,9,9]]),
      (9,'cyclic'): (9406,4646,(18,56,40),38,[[-9,-9,-9],[-9,-9,-9]]),
      (8,'dihedral'): (569,284,(1,0,0),0,[]),
      (9,'dihedral'): (4720,2341,(8,18,12),11,[[]]),
    }
    for (m,g),(total,pairs,rank,remaining,relators) in expected.items():
        with contextlib.redirect_stdout(io.StringIO()):
            v,f,orb,b,active,match,gen,rel=pi1(m,g)
        assert len(orb)==total,(m,g,'cell count')
        assert len(match)==pairs,(m,g,'elementary collapse count')
        result=tuple(sum(len(orb[i])==j+1 for i in active) for j in (0,1,2))
        assert result==rank,(m,g,'residual cell counts',result)
        assert len(gen)==rank[1]-rank[0]+1,(m,g,'spanning tree')
        assert rel==relators,(m,g,'final attaching words',rel)
        if g=='cyclic':
            assert len(set(abs(x) for r in rel for x in r))==1,(m,g,'one surviving circle generator')
        print(f'm={m}, {g}: {total} orbit cells, {pairs} collapses, '
              f'residual {rank}, final relators {rel}')
    print('STABLE_KNESER_HOMOTOPY_CHECK_OK')

if __name__=='__main__':
    verify()
