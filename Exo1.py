from ast import And
from distutils.util import run_2to3
from modulefinder import ReplacePackage


def f(r1,r2,u1,u2):
    if not isinstance (r1,int):
        raise ValueError("r1 doit être un entier")
    if not isinstance (r2,int):
        raise ValueError("r2 doit être un entier")     
    if not isinstance (u1,str):
        raise ValueError("u1 doit être une chaine de caractère")  
    if not isinstance (u2,str):
        raise ValueError("u2 doit être une chaine de caractère")  

    conversion={"m\u2126":1e-3,"\u2126":1,"k\u2126":1e3}
    if u1!="\u2126":
        r1=r1*conversion[u1]
    if u2!="\u2126":
        r2=r2*conversion[u2]
