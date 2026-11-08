"""Finite diagnostics for renewal-age phase coherence (standard library only).

Run: python verify.py
All asymptotic assertions are numerical diagnostics, not substitutes for proof.
"""
from math import sin, pi, isclose, cos


def eta(a, terms=72):
    v = [(j + 1.0)**(-a) for j in range(terms + 1)]
    answer = 0.0
    for k in range(terms):
        answer += v[0] * 2.0**(-k - 1)
        v = [v[j] - v[j + 1] for j in range(len(v) - 1)]
    return answer


def recurrence(alpha, max_n):
    s = [(j + 1)**(-alpha) for j in range(max_n + 1)]
    f = [0.0] + [s[j-1] - s[j] for j in range(1, max_n+1)]
    u = [1.0]
    c = [1.0]
    for n in range(1, max_n + 1):
        u.append(sum(f[k] * u[n-k] for k in range(1,n+1)))
        c.append(sum(((-1)**k)*s[k]*u[n-k] for k in range(n+1)))
    return s, u, c


def age_recursion(alpha, n):
    probs = [1.0]
    observed = [1.0]
    for t in range(1, n + 1):
        new = [0.0] * (len(probs) + 1)
        for a, weight in enumerate(probs):
            hazard = 1.0 - ((a+1.0)/(a+2.0))**alpha
            new[0] += weight*hazard
            new[a+1] = weight*(1.0-hazard)
        probs = new
        observed.append(sum(((-1)**a)*p for a,p in enumerate(probs)))
        assert abs(sum(probs)-1.0)<1e-12
        assert min(probs)>=0.0
    return observed


def run():
    checks=0
    for alpha in (0.25,0.50,0.75):
        s,u,c=recurrence(alpha,4200)
        e=eta(alpha)
        A=sin(pi*alpha)*e/pi
        B=1.0/(2.0*e)
        assert 0<e<1; checks+=1
        assert abs(sum(u[200-j]*s[j] for j in range(201))-1)<2e-12; checks+=1
        independent=age_recursion(alpha,160)
        for n, v in enumerate(independent):
            assert isclose(c[n],v,rel_tol=0,abs_tol=5e-12),(alpha,n,c[n],v)
            checks+=1
        for n in (1000,2000,3000,4200):
            if alpha<0.5:
                target=((-1)**n)*B*n**(-alpha)
                tolerance=0.02
            elif alpha==0.5:
                target=(A+((-1)**n)*B)*n**(-0.5)
                tolerance=0.012
            else:
                target=A*n**(alpha-1)
                tolerance=0.35
            assert abs(c[n]/target-1.0)<tolerance, (alpha,n,c[n],target)
            checks+=1
        if alpha<=0.5:
            for n in (1000,1001,3000,3001,4200):
                assert ((-1)**n)*c[n]>0,(alpha,n,c[n])
                checks+=1
        else:
            for n in (1000,1001,3000,3001,4200):
                assert c[n]>0,(alpha,n,c[n])
                checks+=1
        # An independent age-state recursion checks nontrivial complex gate phases.
        for angle in (pi/3, 0.81*pi):
            z=complex(cos(angle),sin(angle))
            previous=[1.0]
            sshort=[(j+1.0)**(-alpha) for j in range(71)]
            fshort=[0.0]+[sshort[j-1]-sshort[j] for j in range(1,71)]
            ush=[1.0]
            for n in range(1,71):
                ush.append(sum(fshort[k]*ush[n-k] for k in range(1,n+1)))
                new=[0.0]*(len(previous)+1)
                for age,p in enumerate(previous):
                    hazard=1-((age+1.0)/(age+2.0))**alpha
                    new[0]+=p*hazard
                    new[age+1]+=p*(1-hazard)
                previous=new
                first=sum(previous[j]*z**j for j in range(n+1))
                second=sum(ush[n-j]*sshort[j]*z**j for j in range(n+1))
                assert abs(first-second)<5e-12,(alpha,n,angle)
                checks+=1
        print(f'alpha={alpha:.2f}, eta={e:.12f}, recent coefficient={A:.12f}, old coefficient={B:.12f}, n=4200 coherence={c[4200]:.12f}')
    print('PASS:',checks,'independent finite and asymptotic diagnostics')

if __name__=='__main__':
    run()
