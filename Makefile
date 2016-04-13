
xmkgif: xrectangle.c
	    gcc -Wall -lX11 xrectangle.c -o xrectangle -lX11 

install: xmkgif 
	        mkdir -p \${prefix}/usr/local/bin
			cp xmkgif \${prefix}/usr/local/bin
			cp xrectangle \${prefix}/usr/local/bin
