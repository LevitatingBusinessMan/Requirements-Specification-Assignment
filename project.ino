#include <AES.h>
#include <MFRC522.h>
#include <rfid.h>
#define KEYLENGTH 16

RFID rfid;

uint8_t key[KEYLENGTH] = {0xd7, 0xe7, 0xeb, 0x9e, 0x4c, 0xce, 0x25, 0x43, 0x62, 0x91, 0x1b, 0xdd, 0x3d, 0xf2, 0x16, 0xb2};

AES128 aes = AES128();
uint8_t inbuf[16] = {0};
uint8_t outbuf[16] = {0};

void setup() {
  Serial.begin(9600);
  delay(1000);
  rfid.begin();
  aes.setKey(key, KEYLENGTH);
}

void loop() {
  uint32_t uid = rfid.readUID();
  
  //char buf[10];
  //itoa(uid, buf, 16);

  inbuf[0] = uid;
  inbuf[1] = uid >> 8;
  inbuf[2] = uid >> 16;
  inbuf[3] = uid >> 24;
  
  aes.encryptBlock(outbuf,inbuf);

  Serial.write(outbuf,16);

}
