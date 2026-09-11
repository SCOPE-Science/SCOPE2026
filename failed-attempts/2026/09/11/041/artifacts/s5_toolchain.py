import shutil, sys
print("python", sys.version.split()[0])
import sympy; print("sympy", sympy.__version__)
for t in ["sage","magma","gp","pari","mwrank","sageall"]:
    print(t, shutil.which(t))
try:
    import sageall; print("sageall OK")
except Exception as e:
    print("sageall MISSING:", type(e).__name__)
