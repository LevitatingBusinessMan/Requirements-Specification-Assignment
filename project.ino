#include <MD5.h>
#include <SPI.h>
#include <rfid.h>
#include <MFRC522.h>

#define SALT 0xb00b

RFID rfid;

void setup() {
  Serial.begin(9600);
  delay(1000);
  rfid.begin();
}

void loop() {
  uint32_t uid = rfid.readUID();
  
  char buf[10];
  itoa(uid, buf, 16);

  buf[9] = SALT;

  unsigned char* hash = MD5::make_hash(buf, 10);
  char *md5str = MD5::make_digest(hash, 16);
  Serial.println(md5str);

  free(hash);
  free(md5str);

}
