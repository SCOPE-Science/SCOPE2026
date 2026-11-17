"""Numerical cross-checks for rare acute triangles on thin ellipses.

Only finite experiments. Run: python check_ellipse.py
"""
import math
import numpy as np


def uniform_x(n, epsilon, rng):
    x = np.sort(rng.uniform(-1., 1., (n, 3)), axis=1)
    signs = rng.choice(np.array([-1., 1.]), size=(n, 3))
    y = epsilon * signs * np.sqrt(np.maximum(0., 1. - x*x))
    return x, y, signs


def perimeter(n, epsilon, rng):
    x = np.empty((n, 3))
    y = np.empty((n, 3))
    for j in range(3):
        filled = 0
        while filled < n:
            # Uniform angle proposals with acceptance proportional to ellipse speed.
            angles = rng.uniform(0., 2.*math.pi, int((n-filled)*1.75) + 1024)
            speed = np.sqrt(np.sin(angles)**2 + epsilon**2*np.cos(angles)**2)
            angles = angles[rng.random(len(angles)) < speed][:n-filled]
            k = len(angles)
            x[filled:filled+k, j] = np.cos(angles)
            y[filled:filled+k, j] = epsilon*np.sin(angles)
            filled += k
    indices = np.argsort(x, axis=1)
    x = np.take_along_axis(x, indices, axis=1)
    y = np.take_along_axis(y, indices, axis=1)
    return x, y, np.sign(y)


def indicators(x, y):
    dot_left = ((x[:,1]-x[:,0])*(x[:,2]-x[:,0])
                +(y[:,1]-y[:,0])*(y[:,2]-y[:,0]))
    dot_middle = ((x[:,0]-x[:,1])*(x[:,2]-x[:,1])
                  +(y[:,0]-y[:,1])*(y[:,2]-y[:,1]))
    dot_right = ((x[:,0]-x[:,2])*(x[:,1]-x[:,2])
                 +(y[:,0]-y[:,2])*(y[:,1]-y[:,2]))
    return (dot_left > 0.) & (dot_middle > 0.) & (dot_right > 0.)


def test(epsilon, sampler, seed, n=2_400_000):
    rng = np.random.default_rng(seed)
    count=0; x2sum=0; lambda_sum=0; central=0
    for k in range(0,n,120_000):
        size = min(120_000, n-k)
        x,y,signs = sampler(size,epsilon,rng)
        acute = indicators(x,y)
        count += int(acute.sum())
        xx=x[acute]; ss=signs[acute]
        x2sum += float(np.sum(xx[:,1]**2))
        lam = np.log(xx[:,1]-xx[:,0]) / math.log(epsilon)
        lambda_sum += float(lam.sum())
        central += int(np.count_nonzero((ss[:,0]==ss[:,2])&(ss[:,0]!=ss[:,1])))
    p=count/n
    ratio=p/(2.*epsilon**2*math.log(1./epsilon))
    meanx2=x2sum/count
    meanlambda=lambda_sum/count
    fraccentral=central/count
    print(f'{sampler.__name__}: eps={epsilon}, n={n}, acute={count}, p={p:.8g}, '
          f'ratio={ratio:.5f}, EX^2={meanx2:.5f}, Elambda={meanlambda:.5f}, '
          f'central={fraccentral:.5f}')
    # Loose limits appropriate to finite-epsilon, random-error checks.
    assert 0.78 < ratio < 1.14
    assert 0.14 < meanx2 < 0.29
    assert 0.75 < meanlambda < 1.25
    assert fraccentral > 0.84


if __name__ == '__main__':
    test(.018,uniform_x,1)
    test(.018,perimeter,2)
    test(.027,perimeter,3)
    print('THIN_ELLIPSE_ACUTE_LOG_LAW_CHECKS_OK')
