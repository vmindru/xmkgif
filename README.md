#xmkgif
wrapper for byzanz to capture your screen 

```
./xmkgif - wrapper for byzanz
        
        xmkgif with no parameters will check for $DISPLAY var if available and set 
        it will attempt to interact with users other GUI to capture main information.
        Using zenity. If $DISPALY is not set it will simply pritn this help message.

        -d  duration in seconds ( default 10s )
        -D  Delay in seconds ( default 0s )
        -f  Path to the file to store ( default /tmp/gif.gif )
        -c  If mentioned it will record cursor ( default false ) 
        -F  record in full screen mode ( default False ) 
            if not specified draw a rectacnlge area you want to capture

        e.g.:   ./xmkgif  -d 3 /tmp/file.gif - will wait for you to draw
                an rectangle area of your screen that you want to capture,
                record it for 3 second and store it in /tmp/file.gif

                ./xmkgif -F -d 3 /tmp/full_file.gif - note the -F param ,
                this will simply record your entire screen for 3 second and
                store this into /tmp/full_file.gif
 ```

# How To Install 

## Preqreq 

Please install the tools bellow using your favourite package manager 

### byzanz 
tool to capture your desktop and store it in .gif format
https://github.com/GNOME/byzanz 

### zenity
Capture input var's from GUI, used for user interaction.


### Build xreactangle
build xreactangle and copy this somewhere to your $PATH 
`gcc -Wall -lX11 xrectangle.c -o xrectangle -lX11`

### xmkgif - copy this to your path
`cp xmkgif /usr/bin/xmkgif`
or
`cp xmkgif $HOME/bin/xmkgif`

## Wrapper 
__Note:__ Prereq install byzans on your Computer from github or using your favourite package manager 
__xmkgif__ is just a wrapper for byzanz it will help you select a screen area using xtrectangle or capture entire screen 

## TODO: build and publish an RPM

## DEMO CLI
![alt tag](https://raw.githubusercontent.com/vmindru/xrectangle/master/misc/file.gif)
## DEMO GUI - start 
![alt tag](https://raw.githubusercontent.com/vmindru/xrectangle/master/misc/xcapture.gif)
## DEMO GUI - result 
![alt tag](https://raw.githubusercontent.com/vmindru/xrectangle/master/misc/xcapture2.gif) 
## DEMO GUI - partial screen  
![alt tag](https://raw.githubusercontent.com/vmindru/xrectangle/master/misc/xcapture_rectangle.gif) 
