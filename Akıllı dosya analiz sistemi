#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Akıllı Dosya Analiz Sistemi
Seviye 1 — Orta Zor Proje

Bu program, verilen bir klasördeki tüm dosyaları analiz eder:
- Dosya türlerine göre ayırır (uzantı ve kategori bazlı)
- Toplam boyutu hesaplar
- En büyük 10 dosyayı gösterir
- Sonuçları CSV dosyalarına kaydeder
- Hata yönetimi ve loglama yapar

Kullanım:
    python file_analyzer.py <klasör_yolu>
"""

import sys
import logging
from pathlib import Path
from datetime import datetime
import pandas as pd

# Dosya kategorileri (uzantı -> kategori)
CATEGORY_MAP = {
    # Resimler
    '.jpg': 'Image', '.jpeg': 'Image', '.png': 'Image', '.gif': 'Image',
    '.bmp': 'Image', '.tiff': 'Image', '.svg': 'Image', '.webp': 'Image',
    # Videolar
    '.mp4': 'Video', '.avi': 'Video', '.mov': 'Video', '.mkv': 'Video',
    '.flv': 'Video', '.wmv': 'Video', '.webm': 'Video',
    # Ses dosyaları
    '.mp3': 'Audio', '.wav': 'Audio', '.flac': 'Audio', '.aac': 'Audio',
    '.ogg': 'Audio', '.m4a': 'Audio',
    # Dokümanlar
    '.pdf': 'Document', '.doc': 'Document', '.docx': 'Document',
    '.xls': 'Document', '.xlsx': 'Document', '.ppt': 'Document',
    '.pptx': 'Document', '.txt': 'Document', '.rtf': 'Document',
    '.odt': 'Document', '.ods': 'Document',
    # Arşivler
    '.zip': 'Archive', '.rar': 'Archive', '.7z': 'Archive',
    '.tar': 'Archive', '.gz': 'Archive', '.bz2': 'Archive',
    # Kod dosyaları
    '.py': 'Code', '.java': 'Code', '.c': 'Code', '.cpp': 'Code',
    '.js': 'Code', '.html': 'Code', '.css': 'Code', '.json': 'Code',
    '.xml': 'Code', '.sql': 'Code', '.sh': 'Code', '.bat': 'Code',
    # Yürütülebilir
    '.exe': 'Executable', '.msi': 'Executable', '.app': 'Executable',
    '.deb': 'Executable', '.rpm': 'Executable',
    # Diğer
    '.iso': 'DiskImage', '.vmdk': 'DiskImage',
}

class FileAnalyzer:
    """Dosya analiz işlemlerini gerçekleştiren ana sınıf."""
    
    def __init__(self, root_dir):
        """
        Başlangıç ayarları.
        
        Args:
            root_dir (str veya Path): Taranacak ana klasörün yolu.
        """
        self.root_dir = Path(root_dir)
        if not self.root_dir.exists():
            raise FileNotFoundError(f"Klasör bulunamadı: {self.root_dir}")
        if not self.root_dir.is_dir():
            raise NotADirectoryError(f"Geçerli bir klasör değil: {self.root_dir}")
        
        self.files = []          # Tüm dosyaların bilgi listesi (dict)
        self.summary = {}        # Tür bazlı özet istatistikler
        self.total_size = 0      # Toplam boyut (bytes)
        
        # Loglama sistemini kur
        self._setup_logging()
        self.logger = logging.getLogger(__name__)
        
        self.logger.info(f"FileAnalyzer başlatıldı. Hedef klasör: {self.root_dir.resolve()}")
    
    def _setup_logging(self):
        """Loglama ayarlarını yapar (konsol + dosya)."""
        log_format = '%(asctime)s - %(levelname)s - %(message)s'
        logging.basicConfig(
            level=logging.INFO,
            format=log_format,
            handlers=[
                logging.FileHandler('file_analyzer.log', encoding='utf-8'),
                logging.StreamHandler()
            ]
        )
    
    def _get_file_category(self, extension):
        """
        Dosya uzantısına göre kategori döndürür.
        
        Args:
            extension (str): Uzantı (nokta dahil, örn: '.pdf')
            
        Returns:
            str: Kategori adı, tanımsızsa 'Other'
        """
        return CATEGORY_MAP.get(extension.lower(), 'Other')
    
    def _get_file_info(self, file_path):
        """
        Bir dosya için gerekli tüm bilgileri toplar. Hata durumunda None döner.
        
        Args:
            file_path (Path): Dosya yolu
            
        Returns:
            dict veya None: Dosya bilgileri veya hata varsa None
        """
        try:
            stat = file_path.stat()
            size_bytes = stat.st_size
            extension = file_path.suffix
            category = self._get_file_category(extension)
            mod_time = datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
            
            return {
                'path': str(file_path.resolve()),
                'size_bytes': size_bytes,
                'size_mb': round(size_bytes / (1024 * 1024), 2),
                'extension': extension if extension else '(uzantısız)',
                'category': category,
                'modified': mod_time
            }
        except PermissionError:
            self.logger.warning(f"İzin hatası - dosya okunamadı: {file_path}")
        except FileNotFoundError:
            self.logger.warning(f"Dosya bulunamadı (silinmiş olabilir): {file_path}")
        except OSError as e:
            self.logger.warning(f"Dosya okuma hatası ({e}): {file_path}")
        except Exception as e:
            self.logger.error(f"Beklenmeyen hata: {file_path} - {e}")
        return None
    
    def analyze(self):
        """
        Ana analiz işlemini gerçekleştirir:
        - Tüm dosyaları tarar (alt klasörler dahil)
        - Toplam boyutu hesaplar
        - Tür bazında istatistik toplar
        """
        self.logger.info("Analiz başlıyor...")
        self.files.clear()
        self.summary.clear()
        self.total_size = 0
        
        # Geçici tür istatistikleri
        type_stats = {}
        
        # Recursive olarak tüm dosyaları dolaş
        for item in self.root_dir.rglob('*'):
            if item.is_file():
                file_info = self._get_file_info(item)
                if file_info:
                    self.files.append(file_info)
                    self.total_size += file_info['size_bytes']
                    
                    # Tür bazında toplama
                    category = file_info['category']
                    if category not in type_stats:
                        type_stats[category] = {
                            'count': 0,
                            'total_bytes': 0,
                            'extensions': set()
                        }
                    type_stats[category]['count'] += 1
                    type_stats[category]['total_bytes'] += file_info['size_bytes']
                    type_stats[category]['extensions'].add(file_info['extension'])
        
        # Özet bilgileri oluştur
        for cat, data in type_stats.items():
            self.summary[cat] = {
                'count': data['count'],
                'total_bytes': data['total_bytes'],
                'total_mb': round(data['total_bytes'] / (1024 * 1024), 2),
                'extensions': ', '.join(sorted(data['extensions']))
            }
        
        self.logger.info(f"Analiz tamamlandı. Toplam dosya sayısı: {len(self.files)}")
        self.logger.info(f"Toplam boyut: {self.total_size / (1024**3):.2f} GB")
    
    def get_largest_files(self, n=10):
        """
        En büyük n dosyayı döndürür (boyuta göre azalan sırada).
        
        Args:
            n (int): Döndürülecek dosya sayısı
            
        Returns:
            list: En büyük dosyaların bilgilerini içeren liste
        """
        if not self.files:
            self.logger.warning("Henüz analiz yapılmamış. Lütfen önce analyze() çağırın.")
            return []
        sorted_files = sorted(self.files, key=lambda x: x['size_bytes'], reverse=True)
        return sorted_files[:n]
    
    def print_largest_files(self, n=10):
        """En büyük n dosyayı konsola yazdırır."""
        largest = self.get_largest_files(n)
        if not largest:
            print("Dosya bulunamadı veya analiz yapılmadı.")
            return
        
        print("\n" + "="*80)
        print(f" EN BÜYÜK {len(largest)} DOSYA")
        print("="*80)
        for i, file in enumerate(largest, 1):
            print(f"{i:2}. {file['size_mb']:>8.2f} MB  | {file['category']:12} | {file['path']}")
        print("="*80 + "\n")
    
    def print_summary(self):
        """Dosya türlerine göre özet istatistikleri konsola yazdırır."""
        if not self.summary:
            print("Henüz analiz yapılmamış veya hiç dosya bulunamadı.")
            return
        
        print("\n" + "="*80)
        print(" DOSYA TÜRLERİNE GÖRE ÖZET")
        print("="*80)
        print(f"{'Kategori':<15} {'Adet':>8} {'Toplam Boyut (MB)':>20} {'Uzantılar'}")
        print("-"*80)
        for cat, data in sorted(self.summary.items(), key=lambda x: x[1]['total_bytes'], reverse=True):
            print(f"{cat:<15} {data['count']:>8} {data['total_mb']:>20.2f}   {data['extensions']}")
        print("-"*80)
        total_gb = self.total_size / (1024**3)
        print(f" TOPLAM DOSYA SAYISI: {len(self.files)}")
        print(f" TOPLAM BOYUT: {total_gb:.2f} GB ({self.total_size:,} bytes)")
        print("="*80 + "\n")
    
    def save_details_csv(self, output_path="dosya_detaylari.csv"):
        """
        Tüm dosyaların detaylı listesini CSV dosyasına kaydeder.
        
        Args:
            output_path (str): Kaydedilecek CSV dosyasının yolu
        """
        if not self.files:
            self.logger.warning("Kaydedilecek dosya bilgisi yok. Önce analyze() çağırın.")
            return
        
        df = pd.DataFrame(self.files)
        # Sütun sırasını düzenle
        df = df[['path', 'size_bytes', 'size_mb', 'extension', 'category', 'modified']]
        df.to_csv(output_path, index=False, encoding='utf-8')
        self.logger.info(f"Dosya detayları kaydedildi: {output_path}")
    
    def save_summary_csv(self, output_path="dosya_turu_ozet.csv"):
        """
        Dosya türü özetini CSV dosyasına kaydeder.
        
        Args:
            output_path (str): Kaydedilecek CSV dosyasının yolu
        """
        if not self.summary:
            self.logger.warning("Özet bilgisi yok. Önce analyze() çağırın.")
            return
        
        summary_list = []
        for cat, data in self.summary.items():
            summary_list.append({
                'Kategori': cat,
                'Dosya Sayısı': data['count'],
                'Toplam Boyut (MB)': data['total_mb'],
                'Toplam Boyut (Bytes)': data['total_bytes'],
                'Uzantılar': data['extensions']
            })
        df = pd.DataFrame(summary_list)
        df = df.sort_values('Toplam Boyut (MB)', ascending=False)
        df.to_csv(output_path, index=False, encoding='utf-8')
        self.logger.info(f"Özet bilgileri kaydedildi: {output_path}")
    
    def run(self, details_csv="dosya_detaylari.csv", summary_csv="dosya_turu_ozet.csv"):
        """
        Tüm analiz adımlarını çalıştırır ve sonuçları ekrana yazdırır / CSV'ye kaydeder.
        
        Args:
            details_csv (str): Detay CSV dosya adı
            summary_csv (str): Özet CSV dosya adı
        """
        try:
            self.analyze()
            if not self.files:
                print("⚠️ Hiç dosya bulunamadı veya tüm dosyalara erişilemedi.")
                return
            
            self.print_summary()
            self.print_largest_files(10)
            self.save_details_csv(details_csv)
            self.save_summary_csv(summary_csv)
            print(f" Analiz tamamlandı. Log dosyası: file_analyzer.log")
        except Exception as e:
            self.logger.error(f"Analiz sırasında kritik hata: {e}", exc_info=True)
            print(f" Kritik hata: {e}")


def main():
    """Komut satırından çalıştırma için ana fonksiyon."""
    if len(sys.argv) != 2:
        print("Kullanım: python file_analyzer.py <klasör_yolu>")
        print("Örnek: python file_analyzer.py C:\\Users\\Example\\Desktop\\Test")
        sys.exit(1)
    
    folder_path = sys.argv[1]
    
    try:
        analyzer = FileAnalyzer(folder_path)
        analyzer.run()
    except FileNotFoundError as e:
        print(f"Hata: {e}")
        sys.exit(1)
    except NotADirectoryError as e:
        print(f"Hata: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Beklenmeyen hata: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
