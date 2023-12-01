#Identifiers
BM = 0x424D
BA = 0x4241
CI = 0x4349
CP = 0x4350
IC = 0x4943
PT = 0x5054

#DIB Header Types (determines size of header)
BITMAPCOREHEADER = 12
OS21XBITMAPHEADER = 12
#Can be either 64 or 16, if 16 the size is still 64 but all values beyond the first 16 bytes are 0
OS22XBITMAPHEADER = (64,16)
BITMAPINFOHEADER = 40
BITMAPV2INFOHEADER = 52
BITMAPV3INFOHEADER = 56
BITMAPV4HEADER = 108
BITMAPV5HEADER = 124

#Halftoning Compression Options
NONE = 0
ERRORDIFFUSION = 1
PANDA = 2
SUPER_CIRCLE = 3

#Compression Methods
BI_RGB = 0
BI_RLE8 = 1
BI_RLE4 = 2
BI_BITFIELDS = 3
BI_JPEG = 4
BI_PNG = 5
BI_ALPHABITFIELDS = 6
BI_CMYK = 11
BI_CMYKRLE8 = 12
BI_CMYKRLE4 = 13