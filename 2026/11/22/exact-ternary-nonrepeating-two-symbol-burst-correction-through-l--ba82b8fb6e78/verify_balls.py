#!/usr/bin/env python3
"""Direct received-word enumeration, independent of the difference-support test."""
import itertools, json
from pathlib import Path
p=Path(__file__).with_name('codebooks.json')
a=json.loads(p.read_text('utf-8'))
assert a['alphabet']=='012'
for n in range(2,8):
    code=a[str(n)]
    assert len(code)=={2:1,3:1,4:1,5:3,6:6,7:12}[n]
    assert len(code)==len(set(code))
    used={}
    for w in code:
        assert len(w)==n and set(w)<={'0','1','2'}
        assert all(w[i]!=w[i+1] for i in range(n-1))
        outputs={w}
        for start in range(n-1):
            for letters in itertools.product('012', repeat=2):
                y=w[:start]+''.join(letters)+w[start+2:]
                outputs.add(y)
        for y in outputs:
            assert y not in used, (n,w,used.get(y),y)
            used[y]=w
    print('n=',n,'words=',len(code),'distinct reachable outputs=',len(used))
print('VERIFY_OK')
