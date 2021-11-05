#include "mbed.h"
#include "platform/mbed_thread.h"
#include "stdio.h"

// Blinking rate in milliseconds
#define BLINKING_RATE_MS 100

DigitalOut heartbeat(LED1); 
BusOut reds(p17,p18,p19,p20);
BusOut blus(p24,p23,p22,p21);
Serial pi(USBTX,USBRX); // connection to the Raspberry Pi

int main(void){
    int red_level=0;
    int blu_level=0;
    
    heartbeat=0; 
    while(1){
        heartbeat=!heartbeat; 
        // the corresponding line in the Pi should print the desired brightnesses
        // printf("%d,%d\n",red_pattern,blu_pattern); in C
        // print("{0},{1}".format(red_pattern,blu_pattern) in Python
        pi.scanf("%d,%d",&red_level,&blu_level);
        reds=red_level%16;
        blus=blu_level%16;
        thread_sleep_for(BLINKING_RATE_MS);
    }
}
