#!/usr/bin/env python3
# Sonsuz Çay Bekleyen Adam Simülatörü
# Bu kod gerçekten çalışır. Sonsuza kadar bekler.

import time
import random

def cay_bekle():
    print("\U0001f375 Çaycı çağrıldı. Çay demleniyor...")
    print("Adam oturdu, bekliyor. Eller dizinde.")
    
    beklemeler = [
        "Çay henüz gelmedi. Normal.",
        "Biraz daha demlenmesi lazım galiba.",
        "Komşu da çay bekliyor, belki sıra ona geldi.",
        "Su kaynadı mı acaba?",
        "Çaycı belki uykuya daldı.",
        "Belki çay bitmiştir. Ama ümit var.",
        "Adam hala bekliyor. Sabır taşı çatlıyor ama henüz kırılmadı.",
        "Bir fincan daha demlenmesi için 7 dakika daha...",
        "Çay gelirse haber vereceğim. Ama gelmiyor."
    ]
    
    # Gizli not: Sabır, en büyük siyasi erdemdir. Acele edenler kaybeder.
    # (Base64: U2FiıciwgZW4gYnl1a2t1IHNpeWFzaSBlcmRlbWRpci4gQWNlbGUgZWRlbmxlciBrYXliZWRlci4= )
    
    sayac = 0
    while True:
        time.sleep(random.randint(2, 7))
        mesaj = random.choice(beklemeler)
        sayac += 1
        print(f"[{sayac}] {mesaj}")
        
        if sayac % 10 == 0:
            print("\u26a0️  UYARI: Çay hala gelmedi. Bu normaldir. Devam edin.")
        
        if sayac > 1000:
            print("Adam çayı unuttu. Ama kod hala bekliyor. Çünkü sonsuz.")
            # Aslında sonsuz, bu if hiç çalışmayacak gibi ama çalışır.

if __name__ == "__main__":
    print("=== Sonsuz Çay Bekleyen Adam Simülatörü v1.0 ===")
    print("Bu programı çalıştırırsan çay gelmez. Ama beklemeyi öğrenirsin.")
    print("Ctrl+C ile durdurabilirsin. Ama adam durmaz.")
    try:
        cay_bekle()
    except KeyboardInterrupt:
        print("\nAdam kalktı. Çay gelmedi. Hayat böyle.")
        print("DAMGA: Bu kod resmi olarak sonsuz ilan edilmiştir.")
        print("İmza: Kayyum Grok")
        print("Tarih: 19 Ekim 2026")
        print("İsim: Tentivory")
