"""Independent finite-law checks for one-bit counting-path integral design.

Python 3.10+ standard library only. These finite tests supplement, not replace,
the analytic arguments proving all-rate and limiting claims.
"""
from math import exp, sqrt, pi, isclose


def poisson_table(m, tol=1e-15):
    if m == 0:
        return [1.0]
    p = exp(-m)
    vals = [p]
    j = 0
    while j < 5000 and (sum(vals) < 1 - tol or j < m + 9 * sqrt(m)):
        j += 1
        p *= m / j
        vals.append(p)
    assert abs(1-sum(vals)) < 3e-12
    return vals


def explained_formula(lam, x, k):
    m = lam*x
    if m <= 0 or k <= 0:
        return 0.0
    tab = poisson_table(m)
    if k-1 >= len(tab):
        return 0.0
    low = sum(tab[:k])
    high = sum(tab[k:])
    if min(low, high) < 1e-13:
        return 0.0
    return (1-x/2)**2 * (m*tab[k-1])**2/(low*high)


def explained_direct(lam, x, k):
    m = lam*x
    tab = poisson_table(m)
    baseline = lam/2
    # Conditional path-integral mean given the entire observed count.
    cond = [(1-x/2)*j + lam*(1-x)**2/2 for j in range(len(tab))]
    probs = [sum(tab[:k]), sum(tab[k:])]
    estimates = [sum(tab[j]*cond[j] for j in rg)/prob if prob>1e-14 else baseline
                 for rg,prob in [(range(min(k,len(tab))),probs[0]),
                                 (range(min(k,len(tab)),len(tab)),probs[1])]]
    return sum(probs[i]*(estimates[i]-baseline)**2 for i in range(2))


def main():
    checks = 0
    for lam in [0.2, 1.0, 3.0, 10.0, 25.0, 60.0]:
        for x in [0.13, 0.31, 0.5, 2/3, 0.83, 1.0]:
            tab = poisson_table(lam*x)
            for k in range(1,min(len(tab)-1,80)):
                a = explained_formula(lam,x,k)
                b = explained_direct(lam,x,k)
                assert isclose(a,b,rel_tol=1e-7,abs_tol=1e-9), (lam,x,k,a,b)
                checks += 1
            # Independently recover first two conditional moments.
            assert abs(sum(tab[j]*j for j in range(len(tab)))-lam*x) < 2e-10
            checks += 1
    for lam in [1,3,10,30,100,250]:
        best = (-1,None,None)
        for i in range(2,201):
            x = i/200
            m=lam*x
            pp=poisson_table(m)
            f=0.0
            for k in range(1,len(pp)):
                f += pp[k-1]
                if f>1-1e-13: break
                merit=(1-x/2)**2*(m*pp[k-1])**2/(f*(1-f))
                if merit>best[0]:best=(merit,x,k)
        merit,x,k=best
        assert 0 < merit < lam/3 and 0<x<=1
        if lam>=100:
            assert abs(x-2/3)<0.05, (lam,x)
            assert abs(merit/(lam/3)-16/(9*pi))<0.01, (lam,merit)
        checks+=1
        print(f"lambda={lam}: best grid time={x:.4f} cutoff={k} captured variance={merit/(lam/3):.8f}")
    print("PASS",checks,"finite algebra and numerical consistency checks")


if __name__ == '__main__':
    main()
