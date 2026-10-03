---
type: memory
kind: project
name: "master-digit-reconation"
description: "Memory terpusat Digit Reconation — GUI Tkinter gambar angka + prediksi CNN Keras MNIST, plus skrip training"
scope: project
project: "Digit Reconation"
status: archived
updated: 2026-09-25
tags: ["memory/project", "project/Digit Reconation"]
---

# Master Memory Workflow — Digit Reconation

> Memory terpusat proyek ini, disusun 23 September 2026 dari kode. Nama folder memang
> typo **"Reconation"** (seharusnya *Recognition*) — biarkan, banyak path mengacu ke nama ini.
> **Koreksi 2026-09-25:** status git, tanggal commit, dan urutan arsitektur model di bawah diverifikasi
> ulang terhadap `git log`/`git status` dan `train.py`.

**Lokasi:** `C:\Users\Daffa\Desktop\Folder Space AI\Folder Space Semester 6\Digit Reconation`
**Status:** tugas kuliah Semester 6, selesai & kecil.

## Fakta git (diverifikasi 25 Sep 2026)

- **2 commit, keduanya tertanggal 2026-06-12** — bukan "±06-10 s/d 12":
  `e7c9af8` "first commit" (12 Jun 14:49) → `044beb7` "update" (12 Jun 14:51, **HEAD**, author date = commit date).
- **Remote ADA dan tidak pernah disebut di dokumen ini sebelumnya:**
  `origin = https://github.com/daffa-789/Digit-Reconation.git` (branch `main`).
- **HEAD belum ter-push — `main` ahead 1.** `origin/main` masih di `e7c9af8`.
  Catatan penting supaya tidak panik: `044beb7` adalah **commit kosong** — tree-nya identik dengan
  `e7c9af8` (`git diff --name-only e7c9af8 044beb7` = 0 baris, hash tree sama: `9e457d4…`).
  Jadi tidak ada karya yang tertahan di lokal; yang belum naik cuma penanda commit saja.
- **Working tree TIDAK lagi bersih**: 1 entri untracked, yaitu `Master_Memory_Workflow.md` (berkas ini).
  Tiga file ter-track: `main.py`, `train.py`, `.gitignore`.
**Koreksi 2026-09-25:** R1 lama menulis "Git bersih, 2 commit (±2026-06-10 s/d 12)". Angka 06-10 itu
**bukan tanggal commit** — itu mtime `main.py` (2026-06-10 14:56). Kedua commit benar-benar terjadi di
hari yang sama, 2026-06-12, selisih 2 menit. "Git bersih" juga sudah tidak berlaku sejak berkas ini
dibuat.

## R1. Angka Kunci

| Aspek | Nilai |
|---|---|
| Bentuk | 2 file Python datar, ±144 baris |
| Stack | Python + `tensorflow`/Keras + `Pillow` + `numpy` + `tkinter` (stdlib) |
| Model | `digit_model.keras` (2,7 MB / 2.755.313 B, **sudah tersedia — tapi HANYA di mesin ini**) |
| Arsitektur model | CNN Sequential kustom, 10 lapis (urutan nyata di `train.py:13-26`):<br>`Conv2D 32 (3×3, relu, in 28×28×1)` → **`BatchNormalization`** → `MaxPooling2D (2×2)` → `Conv2D 64 (3×3, relu)` → **`BatchNormalization`** → `MaxPooling2D (2×2)` → `Flatten` → `Dense 128 relu` → `Dropout 0.3` → `Dense 10 softmax`.<br>Compile: `adam` + `sparse_categorical_crossentropy` + metrik `accuracy`; training **5 epoch** di MNIST yang sudah di-reshape ke `(-1,28,28,1)` dan dinormalisasi /255 |
| Dependensi | ❌ tidak ada `requirements.txt` |
| `.gitignore` | mengabaikan `digit_model.keras` dan `.qodo/` → model tidak masuk repo |

**Koreksi 2026-09-25:** baris arsitektur versi lama (`Conv2D 32 → Conv2D 64 + BatchNorm → MaxPool →
Dense 128 → …`) hanya mencatat **satu** BatchNorm dan **satu** MaxPool, padahal `train.py` memasang
**dua BatchNorm + dua MaxPool** (setiap blok Conv punya pasangannya sendiri) dan melewatkan `Flatten`
di antara MaxPool kedua dan Dense 128. Baris `.gitignore` sudah benar — isinya persis `/.qodo` dan
`/digit_model.keras`.

## R2. Alur

`train.py` → unduh MNIST, latih 5 epoch, simpan `digit_model.keras`.
`main.py` (`SmoothDigitRecognizerApp`) → kanvas kuas 280 px → **invert → auto-crop → resize 20 →
pad ke 28×28 → normalisasi → `model.predict`** → tampilkan digit + confidence %.

Preprocessing-nya benar secara MNIST (latar putih→hitam, digit putih di tengah 28×28) — itu
sebabnya akurasinya masuk akal untuk kuas manual.

## R3. Cara Menjalankan

```bash
python train.py     # opsional HANYA di mesin ini (model ada) — wajib di mesin lain, model tak ter-track
python main.py      # butuh display (GUI Tkinter)
```
**Wajib dijalankan dari dalam folder proyek** — `main.py` memakai path relatif
`'digit_model.keras'` dan memanggil `exit()` bila model tidak ketemu.

## R4. Konvensi

- Path relatif + komentar Bahasa Indonesia.
- Tidak ada config; parameter training hardcoded di `train.py` (epoch=5).

## R5. Gotchas

- 🔴 **Model yang dikirim TIDAK divalidasi terhadap skrip training sekarang.** `digit_model.keras`
  ber-mtime **2026-06-08 12:09**, sedangkan `train.py` terakhir diubah **2026-06-12 13:49** — berkas
  arsitektur itu diedit **±4 hari setelah** model dilatih. Artinya angka accuracy yang pernah dilihat
  waktu itu adalah milik versi script lama, bukan dari `train.py` yang ada sekarang. Klaim apa pun
  tentang kualitas prediksi model ini **belum terverifikasi**; satu-satunya cara membuktikannya adalah
  `python train.py` ulang (5 epoch, otomatis mencetak validation accuracy di akhir) lalu bandingkan,
  atau perlakukan model sekarang sebagai "kira-kira jalan".
  Bukti tidak tersimpan di mana pun: tidak ada log training, tidak ada notebook, dan repo hanya
  men-track 3 file.
- **Model tidak ter-track git** (`.gitignore` baris 2 `/digit_model.keras`), jadi hasil clone dari
  `github.com/daffa-789/Digit-Reconation` **tidak punya model sama sekali** → `main.py` mencetak
  "File 'digit_model.keras' tidak ditemukan!" lalu `exit()` (`main.py:8-11`). Wajib
  `python train.py` dulu di mesin baru (butuh download MNIST, jadi perlu internet pada langkah itu).
- Tanpa `requirements.txt`: instal `tensorflow` versi baru bisa mengubah API `keras` — kunci versi bila proyek dihidupkan.
- Butuh GUI; tidak cocok dijalankan di headless/CI.

## R6. Aturan Memory Proyek Ini

Berkas ini satu-satunya memory terpusat proyek. Perubahan berarti dicatat di sini.

---

## Peta Dokumen Proyek

Berkas ini adalah **satu-satunya memory terpusat** untuk proyek `Digit Reconation`.
Perubahan berarti dicatat di sini lewat commit `docs(memory): catat …`.

### Diserap ke arsip di bawah (file aslinya dihapus)
- (tidak ada — proyek ini tidak punya markdown lain untuk diserap)

### Dibiarkan (bukan memory)
- (tidak ada)

---

## Arsip Dokumen Sumber (verbatim)

Isi setiap sumber dipertahankan apa adanya; separator hanya menandai batas antar dokumen.
Diarsipkan saat konsolidasi memory 2026-09-23 (generator satu-kali pakai, sudah dihapus)

<!-- ARCHIVE-BEGIN -->
<!-- ARCHIVE-END -->
