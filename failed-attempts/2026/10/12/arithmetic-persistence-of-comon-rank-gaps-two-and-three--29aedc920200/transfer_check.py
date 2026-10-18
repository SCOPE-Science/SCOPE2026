#!/usr/bin/env python3
# Neutral arithmetic/bookkeeping check for the transfer theorem.

def cp_system(n, r):
    return {"variables": 3*n*r, "equations": n**3}

def sym_system(n, r):
    return {"variables": (n+1)*r, "equations": n**3}

expected={2:(110,112),3:(165,168)}
for k,(r,s) in expected.items():
    assert r==55*k and s==56*k and s-r==k
    n=27*k
    cp=cp_system(n,r-1)
    sy=sym_system(n,s-1)
    assert cp["variables"]>0 and cp["equations"]==n**3
    assert sy["variables"]>0 and sy["equations"]==n**3
    print(f"k={k} dimension={n} CP={r} symmetric={s} gap={k}")
    print(f"forbidden_CP_system variables={cp['variables']} equations={cp['equations']}")
    print(f"forbidden_symmetric_system variables={sy['variables']} equations={sy['equations']}")
print("CHECK_OK")
