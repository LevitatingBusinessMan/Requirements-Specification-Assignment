#include <AES.h>
#include <MFRC522.h>
#include <rfid.h>
#define KEYLENGTH 16

RFID rfid;

uint8_t key[KEYLENGTH] = {0xd7, 0xe7, 0xeb, 0x9e, 0x4c, 0xce, 0x25, 0x43, 0x62, 0x91, 0x1b, 0xdd, 0x3d, 0xf2, 0x16, 0xb2};

AES128 aes = AES128();

void setup() {
  Serial.begin(9600);
  delay(1000);
  rfid.begin();
  aes.setKey(key, KEYLENGTH);
}

void loop() {
  if (Serial.available() < 4) return;

  uint8_t IV[4] = {0};
  uint8_t block[16] = {0};
  
  Serial.readBytes(IV, 4);

  uint32_t uid = rfid.readUID();

  block[0] = uid ^ IV[0];
  block[1] = (uid >> 8) ^ IV[1];
  block[2] = (uid >> 16) ^ IV[2];
  block[3] = (uid >> 24) ^ IV[3];

  // Add the IV to the plaintext as a canary
  memcpy(block + 4, IV, 4);

  aes.encryptBlock(block,block);

  Serial.write(block,16);
  Serial.flush();
}
