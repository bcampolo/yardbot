# RASPBERRY PI 4 MODEL B   PIN LAYOUT
```
                                 ╭───╮              
                         +3V3  1 │o o│  2 +5V
             (I2C1 SDA) GPIO2  3 │o o│  4 +5V
            (I2C1 SCL1) GPIO3  5 │o o│  6 GROUND
               (GPCLK0) GPIO4  7 │o o│  8 GPIO14 (UART TX0)
                       GROUND  9 │o o│ 10 GPIO15 (UART RX0)
                       GPIO17 11 │o o│ 12 GPIO18 (PCM CLK)
                       GPIO27 13 │o o│ 14 GROUND
                       GPIO22 15 │o o│ 16 GPIO23
                         +3V3 17 │o o│ 18 GPIO24
           (SPI0_MOSI) GPIO10 19 │o o│ 20 GROUND
           (SPI0_MISO)  GPIO9 21 │o o│ 22 GPIO25
           (SPI0_SCLK) GPIO11 23 │o o│ 24 GPIO8 (SPI0_CE0)
                       GROUND 25 │o o│ 26 GPIO7 (SPI0_CE1)
  (Reserved EEPROM SDA) GPIO0 27 │o o│ 28 GPIO1 (Reserved EEPROM SDL)
                        GPIO5 29 │o o│ 30 GROUND
                        GPIO6 31 │o o│ 32 GPIO12 (PWM0)
                (PWM1) GPIO13 33 │o o│ 34 GROUND
                       GPIO19 35 │o o│ 36 GPIO16
              (PCM FS) GPIO26 37 │o o│ 38 GPIO20 (PCM DIN)
                       GROUND 39 │o o│ 40 GPIO21 (PCM DOUT)
                                 ╰───╯              
```
