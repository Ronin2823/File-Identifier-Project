import sys
import pathlib as path 

# Lits of all signature files and magic numbers
SIGNATURES = [
#Documents
(b"%PDF-", "PDF"),
(b"\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1", "MS Office (DOC, XLS, PPT - legacy)"),
(b"PK\x03\x04", "DOCX / XLSX / PPTX (ZIP-based)"),
(b"{\\rtf", "RTF"),
#------------------------------------
#Images
(b"\x89PNG\r\n\x1a\n", "PNG"),
(b"\xFF\xD8\xFF", "JPEG"),
(b"GIF87a", "GIF"),
(b"GIF89a", "GIF"),
(b"BM", "BMP"),
(b"II*\x00" "TIFF (little endian)"),
(b"MM\x00*", "TIFF (big endian)"),
(b"\x00\x00\x01\x00", "ICO"),
(b"RIFF", "WEBP (needs deeper check)"),
#------------------------------------
#Audio
(b"ID3", "MP3 (ID3 tag)"),
(b"\xFF\xFB", "MP3 (frame sync)"),
(b"OggS", "OGG"),
(b"fLaC", "FLAC"),
(b"RIFF", "WAV (needs format check)"),
(b"MThd", "MIDI"),
#------------------------------------
#Video
(b"\x00\x00\x00\x18ftypmp42", "MP4"),
(b"\x00\x00\x00\x20ftypisom", "MP4"),
(b"\x1A\x45\xDF\xA3", "MKV / WebM"),
(b"RIFF", "AVI"),
(b"FLV", "Flash Video"),
#------------------------------------
#Archives
(b"PK\x03\x04", "ZIP"),
(b"Rar!\x1A\x07\x00", "RAR"),
(b"7z\xBC\xAF\x27\x1C", "7-Zip"),
(b"\x1F\x8B\x08", "GZIP"),
(b"BZh", "BZIP2"),
(b"\xFD7zXZ\x00", "XZ"),
(b"ustar", "TAR (offset-based)"),
#------------------------------------
#Executables & Binaries
(b"\x7FELF", "Linux ELF"),
(b"MZ", "Windows EXE / DLL"),
(b"\xFE\xED\xFA\xCE", "Mach-O (macOS, 32-bit"),
(b"\xFE\xED\xFA\xCF", "Mach-O (macOS, 64-bit"),
(b"\xCA\xFE\xBA\xBE", "Mach-O Fat Binary"),
#------------------------------------
#Scripts / Text-Based (Heuristic)
(b"#!/bin/bash", "Bash script"),
(b"#!/usr/bin/env python", "Python script"),
(b"<?xml", "XML"),
(b"<!DOCTYPE html", "HTML"),
(b"{\n", "JSON (heuristic)"),
#------------------------------------
#Certificates / Crypto
(b"-----BEGIN CERTIFICATE-----", "PEM certificate"),
(b"-----BEGIN RSA PRIVATE KEY-----", "RSA key"),
(b"ssh-rsa", "SSH public key")
]

