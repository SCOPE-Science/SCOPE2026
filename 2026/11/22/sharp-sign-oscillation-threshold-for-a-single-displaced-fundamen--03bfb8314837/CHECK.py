"""Supplementary numerical checks of a sharp one-defect Fourier oscillation law.

The complete theorem is proved analytically in RESULT.md. This finite checker
verifies formulas and partial Fourier synthesis, not infinite positivity.
Requires Python 3 standard library only.
"""
import math

N = 4096
count = 0
for alpha in (0.2, 0.5, 0.6, 0.7):
    r = alpha**2 / (1.0 - alpha**2)
    a = math.pi * alpha / math.sin(math.pi*alpha)
    assert 0 < r < 1
    # Exactly, the constant coefficient is 1 and the first cosine
    # coefficient is 2*r. These are numerical consistency checks.
    c0 = a * math.sin(math.pi*alpha) / (math.pi*alpha)
    c1 = a * 2*alpha*math.sin(math.pi*alpha) / (math.pi*(1-alpha**2))
    assert abs(c0 - 1) < 1e-13
    assert abs(c1 - 2*r) < 1e-13
    count += 3
    for j in range(41):
        t = -math.pi + 2*math.pi*j/40
        x = math.cos(t)
        expected = (1-r*r)/(1-2*r*x+r*r)
        # Fast trigonometric recurrence; absolute convergence also gives
        # a rigorous tail bound <= 2*alpha**2/(N-1) + 2*r**(N+1)/(1-r).
        s = a*math.cos(alpha*t)
        cs, cs1 = 1.0, x
        rr = r*r
        for n in range(2, N+1):
            cs2 = 2*x*cs1-cs
            cs, cs1=cs1,cs2
            c = 2*rr + 2*((-1)**n)*alpha**2/(n*n-alpha*alpha)
            s += c*cs2
            rr *= r
        bound = 2*alpha**2/(N-1) + (2*r**(N+1)/(1-r) if r>0 else 0)
        assert abs(s-expected)<bound + 1e-9, (alpha,t,s,expected,bound)
        assert expected > 0
        count+=2
for alpha in (1/math.sqrt(2), 0.75, 0.85, 0.97):
    # The sign-definite test integral is strictly negative for alpha>
    # the endpoint, and exactly zero at alpha=1/sqrt(2).
    m0=math.sin(math.pi*alpha)/(math.pi*alpha)
    m1=alpha*math.sin(math.pi*alpha)/(math.pi*(1-alpha**2))
    assert m0>0 and m1 >= m0-1e-12
    count+=1
print('CHECK_OK supplementary_assertions=', count)
