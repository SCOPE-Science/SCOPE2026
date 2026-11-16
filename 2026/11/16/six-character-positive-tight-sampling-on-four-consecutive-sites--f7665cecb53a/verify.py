"""Finite numerical corroboration of six-positive-frequency quadrature; not a proof."""
import numpy as np
for p in [7, 11, 13, 17, 19, 23, 29, 31]:
    a = [0, p // 3, (2*p+2) // 3]
    eta = np.exp(2j*np.pi*np.array(a)/p)
    mat = np.array([[1,1,1], eta.real, eta.imag])
    alpha = np.linalg.solve(mat, np.array([1.,0.,0.]))
    assert min(alpha)>0
    z=[]
    for k in a:
        t=np.exp(2j*np.pi*k/(2*p))
        z.extend((t,-t))
    w=np.repeat(alpha/2,2)
    assert abs(sum(w)-1.)<1e-12
    for k in (1,2,3):
        assert abs(sum(w*np.array(z)**k))<1e-12
print('SIX_NODE_POSITIVE_FRAME_PASS')
