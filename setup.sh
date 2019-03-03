#!/usr/bin/env bash

BINDIR="$HOME/bin"


if [ ! -d "$BINDIR" ]
then
    echo "creating BINDIR: $BINDIR"
    mkdir -p $BINDIR
else
    echo "BINDIR: $BINDIR already exists"
fi


if [ ! -f $BINDIR/xmkgif ]
then
    echo "copy files xmkgif"
    cp ./xmkgif $BINDIR
    echo "chmod u+x xmkgif"
    chmod u+x $BINDIR/xmkgif
else
    echo "file $BINDIR/xmkgif already exist"
fi

if [ ! -f $BINDIR/xmkgif-stop ]
then
    echo "copy files xmkgif-stop"
    cp ./xmkgif-stop $BINDIR
    echo "chmod u+x xmkgif-stop"
    chmod u+x $BINDIR/xmkgif-stop
else
    echo "file $BINDIR/xmkgif-setup already exist"
fi


