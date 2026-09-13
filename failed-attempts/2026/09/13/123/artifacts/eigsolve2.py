"""Stable generalized eigensolve without Cholesky: use eigsh on scaled + shift-invert,
or power iteration / Lanczos in float64 on the whitened pencil via SVD of Is.
Approach: Is = U S U' (eigh, float64 after rescale). Whiten with threshold; then
Y = S^{-1/2}U' Js U S^{-1/2}; top eig of Y by eigh. Rescale first: divide I,J by I[0,0]
to bring entries to O(1)."""
import numpy as np
I=np.load("output/artifacts/I_mat.npy"); J=np.load("output/artifacts/J_mat.npy")
print("shapes", I.shape)
s0=I[0,0]
In=I/s0; Jn=J/s0
print("In range: %.3e .. %.3e" % (In.min(), In.max()))
print("Jn range: %.3e .. %.3e" % (Jn.min(), Jn.max()))
# scale rows/cols by sqrt diag
dd=np.sqrt(np.diag(In))
Is=In/dd[:,None]/dd[None,:]; Js=Jn/dd[:,None]/dd[None,:]
print("cond proxy: max|Is|=%.3e min diag=1" % (abs(Is).max()))
s,U=np.linalg.eigh((Is+Is.T)/2)
print("eig(Is): min=%.6e max=%.6e  (#<1e-12: %d)" % (s.min(), s.max(), (s<1e-12).sum()))
# whiten keeping modes with s>1e-10
keep=s>1e-10
print("kept:", keep.sum())
Uk=U[:,keep]; sk=s[keep]
Wm=(Uk/sk[None,:])  # U S^{-1}... Y = S^{-1/2} U' Js U S^{-1/2}
A=(Uk*np.sqrt(1/sk)[None,:])
Y=A.T@((Js+Js.T)/2)@A
w,V=np.linalg.eigh(Y)
print("top 12 generalized eigs:", w[-12:])
print("max M =", w[-1])
np.save("output/artifacts/eigvals.npy", w)
c=(A@V[:,-1])/dd
c=c*(1.0/c[np.argmax(np.abs(c))])
np.save("output/artifacts/coeff_float.npy", c)
print("Rayleigh:", (c@J@c)/(c@I@c))
print("coeff range:", np.abs(c).min(), np.abs(c).max())
