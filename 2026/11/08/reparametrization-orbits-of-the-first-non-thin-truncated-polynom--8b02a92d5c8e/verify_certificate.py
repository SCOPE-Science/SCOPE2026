"""Replay the explicit finite-orbit certificate (requires verify.py nearby)."""
import json
from collections import Counter, deque
from pathlib import Path
from verify import Field,N

certificate=json.loads(Path(__file__).with_name('orbit_certificate.json').read_text(encoding='utf-8'))
all_reps=certificate['representatives']
for q in (2,4):
    F=Field(q)
    gens=[F.powers(m,c) for m in range(2,N) for c in ([1] if q==2 else [1,2])]
    if q==4:gens.append(F.scaling(2))
    covered=set()
    totals=Counter()
    size_dist={1:Counter(),2:Counter()}
    reps=[r for r in all_reps if r['q']==q]
    for rep in reps:
        k=rep['stratum']
        B=F.normal_form(k,rep['parameters'])
        assert B not in covered
        orbit={B}; queue=deque([B])
        while queue:
            old=queue.popleft()
            for pw in gens:
                new=F.basis([F.substitute(v,pw) for v in old])
                if new not in orbit:
                    orbit.add(new);queue.append(new)
        assert len(orbit)==rep['size']
        assert not orbit.intersection(covered)
        covered.update(orbit)
        totals[k]+=len(orbit)
        size_dist[k][len(orbit)]+=1
    assert len(covered)==(q**7-q**6)+(q**5-q**4)
    assert totals[1]==q**7-q**6 and totals[2]==q**5-q**4
    print(q,'orbits',len(reps),'sizes',{k:dict(size_dist[k]) for k in (1,2)})
print('VERIFY_OK')
