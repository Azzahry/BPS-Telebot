from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "7139442435:AAHuWz7btk8hz_GG2vXcL7bEO4HtUY2ObQI"
USERNAME_BOT = "BPSKABMALANG_bot"

#initialize command
async def start_command(update:Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_photo(caption='Selamat datang.\nSaya adalah chat bot BPS. Silahkan ikuti panduan berikut untuk berinteraksi dengan chatbot\n----------------\nUntuk mengakses menu pada chatbot ini, anda bisa mengetikkan /menu atau mengklik tombol menu di pojok kiri bawah')

async def dashboard_command(update:Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Selamat Datang \nChatbot BPS Kabupaten Malang\n----------------\nPilih Layanan Informasi : \n1. Pusat Statistik Terpadu (PST) Online \n2. Panduan Konsultasi Statistik \n3. Data Statistik \n4. Pojok Statistik\n5. Saran dan Pengaduan\n----------------\nUntuk memilih layanan, silahkan ketikkan format berikut: /bps (pilihan anda).\nContoh :/bps 1')

async def error(update:Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'error : {context.error}')
#---------------------------------------

#content menu
async def pst_menu(update: Update):
    await update.message.reply_photo(photo='image/logo-or-header/logo-pst.png', caption='Selamat Datang! \nPelayanan Statistik Terpadu (PST) Online 📲 \n----------------\nBerikut link website PST Online : http://perpustakaan.bps.go.id \n----------------\nKlik atau ketikkan /menu untuk kembali ke halaman menu')

async def data_statistik(update: Update):
    await update.message.reply_photo(photo='image/logo-or-header/statistics-header.jpg', caption='Selamat Datang! \nData Statistik 📊 \nData Statistik merupakan layanan informasi mengenai pendataan BPS Kabupaten Malang\n----------------\nPilih Layanan Informasi : \n• Sosial dan kependudukan [sk] \n• Ekonomi dan Perdagangan [ep] \n• Pertanian dan Pertambangan [pp] \n----------------\nUntuk memilih layanan, silahkan ketikkan format berikut: /bps (pilihan anda).\n Contoh :/bps sk')

async def pojok_statistik(update: Update):
    await update.message.reply_photo(photo='image/logo-or-header/pojokstatistik.png', caption='Selamat Datang! \nLayanan Pojok Statistik 📊 \n----------------\nSilahkan hubungi nomor berikut: \nhttps://wa.me/6289654993852 \n----------------\nKlik atau ketikkan /menu untuk kembali ke halaman menu')

async def saran_pengaduan(update: Update):
    await update.message.reply_photo(photo='image/logo-or-header/complain-logo.jpg', caption='Selamat Datang! \nSaran dan Pengaduan 📊 \n----------------\nUntuk saran dan pengaduan anda, mengirimkan ke alamat email berikut ini: \npengaduan3507@bps.go.id \n---------------\nKlik atau ketikkan /menu untuk kembali ke halaman menu')
#-----------------------------------------

#sub-content function
async def konsultasi_statistik(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_diterima: str = update.message.text.lower()
    if 'ks 1' in text_diterima:
        await update.message.reply_photo(photo='image/logo-or-header/konsul-1-min.png', caption='Klik atau ketikkan /menu untuk kembali ke halaman menu')
    elif 'ks 2' in text_diterima:
        await update.message.reply_photo(photo='image/logo-or-header/konsul-2-min.png', caption='Klik atau ketikkan /menu untuk kembali ke halaman menu')
    elif 'ks 3' in text_diterima:
        await update.message.reply_photo(photo='image/logo-or-header/konsul-3-min.png', caption='Klik atau ketikkan /menu untuk kembali ke halaman menu')
    elif 'ks 4' in text_diterima:
        await update.message.reply_photo(photo='image/logo-or-header/konsul-4-min.png', caption='Klik atau ketikkan /menu untuk kembali ke halaman menu')
    elif 'ks 5' in text_diterima:
        await update.message.reply_photo(photo='image/logo-or-header/konsul-5-min.png', caption='Klik atau ketikkan /menu untuk kembali ke halaman menu')

async def sosial_kependudukan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_diterima: str = update.message.text.lower()
    if 'sk 1' in text_diterima:
        await update.message.reply_text('https://malangkab.bps.go.id/subject/108/agama.html#subjekViewTab3 \n----------------\nKlik atau ketikkan /menu untuk kembali ke halaman menu')
    elif 'sk 2' in text_diterima:
        await update.message.reply_text('https://malangkab.bps.go.id/subject/40/gender.html#subjekViewTab3 \n----------------\nKlik atau ketikkan /menu untuk kembali ke halaman menu')
    elif 'sk 3' in text_diterima:
        await update.message.reply_text('https://malangkab.bps.go.id/subject/153/geografi.html#subjekViewTab3 \n----------------\nKlik atau ketikkan /menu untuk kembali ke halaman menu')
    elif 'sk 4' in text_diterima:
        await update.message.reply_text('https://malangkab.bps.go.id/subject/154/iklim.html#subjekViewTab3 \n----------------\nKlik atau ketikkan /menu untuk kembali ke halaman menu')
    elif 'sk 5' in text_diterima:
        await update.message.reply_text('https://malangkab.bps.go.id/subject/26/indeks-pembangunan-manusia.html#subjekViewTab3 \n----------------\nKlik atau ketikkan /menu untuk kembali ke halaman menu')
    elif 'sk 6' in text_diterima:
        await update.message.reply_text('https://malangkab.bps.go.id/subject/23/kemiskinan-dan-ketimpangan.html#subjekViewTab3 \n----------------\nKlik atau ketikkan /menu untuk kembali ke halaman menu')
    elif 'sk 7' in text_diterima:
        await update.message.reply_text('https://malangkab.bps.go.id/subject/12/kependudukan.html#subjekViewTab3 \n----------------\nKlik atau ketikkan /menu untuk kembali ke halaman menu')
    elif 'sk 8' in text_diterima:
        await update.message.reply_text('https://malangkab.bps.go.id/subject/30/kesehatan.html#subjekViewTab3 \n----------------\nKlik atau ketikkan /menu untuk kembali ke halaman menu')
    elif 'sk 9' in text_diterima:
        await update.message.reply_text('https://malangkab.bps.go.id/subject/5/konsumsi-dan-pengeluaran.html#subjekViewTab3 \n----------------\nKlik atau ketikkan /menu untuk kembali ke halaman menu')
    elif 'sk 10' in text_diterima:
        await update.message.reply_text('https://malangkab.bps.go.id/subject/152/lingkungan-hidup.html#subjekViewTab3 \n----------------\nKlik atau ketikkan /menu untuk kembali ke halaman menu')
    elif 'sk 11' in text_diterima:
        await update.message.reply_text('https://malangkab.bps.go.id/subject/101/pemerintahan.html#subjekViewTab3 \n----------------\nKlik atau ketikkan /menu untuk kembali ke halaman menu')
    elif 'sk 12' in text_diterima:
        await update.message.reply_text('https://malangkab.bps.go.id/subject/28/pendidikan.html#subjekViewTab3 \n----------------\nKlik atau ketikkan /menu untuk kembali ke halaman menu')
    elif 'sk 13' in text_diterima:
        await update.message.reply_text('https://malangkab.bps.go.id/subject/29/perumahan.html#subjekViewTab3 \n----------------\nKlik atau ketikkan /menu untuk kembali ke halaman menu')
    elif 'sk 14' in text_diterima:
        await update.message.reply_text('https://malangkab.bps.go.id/subject/34/politik-dan-keamanan.html#subjekViewTab3 \n----------------\nKlik atau ketikkan /menu untuk kembali ke halaman menu')
    elif 'sk 15' in text_diterima:
        await update.message.reply_text('https://malangkab.bps.go.id/subject/27/sosial-budaya.html#subjekViewTab3 \n----------------\nKlik atau ketikkan /menu untuk kembali ke halaman menu')
    elif 'sk 16' in text_diterima:
        await update.message.reply_text('https://malangkab.bps.go.id/subject/6/tenaga-kerja.html#subjekViewTab3 \n----------------\nKlik atau ketikkan /menu untuk kembali ke halaman menu')
    else:
        return await update.message.reply_text('Pilihan tidak ada / valid. Silahkan ketikkan kembali pilihan anda (SK)')

async def ekonomi_perdagangan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_diterima: str = update.message.text.lower()
    if 'ep 1' in text_diterima:
        await update.message.reply_text('https://malangkab.bps.go.id/subject/8/ekspor-impor.html#subjekViewTab3 \n----------------\nKlik atau ketikkan /menu untuk kembali ke halaman menu')
    elif 'ep 2' in text_diterima:
        await update.message.reply_text('https://malangkab.bps.go.id/subject/7/energi.html#subjekViewTab3 \n----------------\nKlik atau ketikkan /menu untuk kembali ke halaman menu')
    elif 'ep 3' in text_diterima:
        await update.message.reply_text('https://malangkab.bps.go.id/subject/102/harga-eceran.html#subjekViewTab3 \n----------------\nKlik atau ketikkan /menu untuk kembali ke halaman menu')
    elif 'ep 4' in text_diterima:
        await update.message.reply_text('https://malangkab.bps.go.id/subject/36/harga-produsen.html#subjekViewTab3 \n----------------\nKlik atau ketikkan /menu untuk kembali ke halaman menu')
    elif 'ep 5' in text_diterima:
        await update.message.reply_text('https://malangkab.bps.go.id/subject/9/industri.html#subjekViewTab3 \n----------------\nKlik atau ketikkan /menu untuk kembali ke halaman menu')
    elif 'ep 6' in text_diterima:
        await update.message.reply_text('https://malangkab.bps.go.id/subject/3/inflasi.html#subjekViewTab3 \n----------------\nKlik atau ketikkan /menu untuk kembali ke halaman menu')
    elif 'ep 7' in text_diterima:
        await update.message.reply_text('https://malangkab.bps.go.id/subject/13/keuangan.html#subjekViewTab3 \n----------------\nKlik atau ketikkan /menu untuk kembali ke halaman menu')
    elif 'ep 8' in text_diterima:
        await update.message.reply_text('https://malangkab.bps.go.id/subject/2/komunikasi.html#subjekViewTab3 \n----------------\nKlik atau ketikkan /menu untuk kembali ke halaman menu')
    elif 'ep 9' in text_diterima:
        await update.message.reply_text('https://malangkab.bps.go.id/subject/16/pariwisata.html#subjekViewTab3 \n----------------\nKlik atau ketikkan /menu untuk kembali ke halaman menu')
    elif 'ep 10' in text_diterima:
        await update.message.reply_text('https://malangkab.bps.go.id/subject/52/produk-domestik-regional-bruto.html#subjekViewTab3 \n----------------\nKlik atau ketikkan /menu untuk kembali ke halaman menu')
    elif 'ep 11' in text_diterima:
        await update.message.reply_text('https://malangkab.bps.go.id/subject/17/transportasi.html#subjekViewTab3 \n----------------\nKlik atau ketikkan /menu untuk kembali ke halaman menu')
    elif 'ep 12' in text_diterima:
        await update.message.reply_text('https://malangkab.bps.go.id/subject/19/upah--buruh.html#subjekViewTab3 \n----------------\nKlik atau ketikkan /menu untuk kembali ke halaman menu')

async def pertanian_pertambangan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_diterima: str = update.message.text.lower()

    if 'pp 1' in text_diterima:
        await update.message.reply_text('https://malangkab.bps.go.id/subject/55/hortikultura.html#subjekViewTab3 \n----------------\nKlik atau ketikkan /menu untuk kembali ke halaman menu')
    elif 'pp 2' in text_diterima:
        await update.message.reply_text('https://malangkab.bps.go.id/subject/60/kehutanan.html#subjekViewTab3 \n----------------\nKlik atau ketikkan /menu untuk kembali ke halaman menu')
    elif 'pp 3' in text_diterima:
        await update.message.reply_text('https://malangkab.bps.go.id/subject/56/perikanan.html#subjekViewTab3 \n----------------\nKlik atau ketikkan /menu untuk kembali ke halaman menu')
    elif 'pp 4' in text_diterima:
        await update.message.reply_text('https://malangkab.bps.go.id/subject/54/perkebunan.html#subjekViewTab3 \n----------------\nKlik atau ketikkan /menu untuk kembali ke halaman menu')
    elif 'pp 5' in text_diterima:
        await update.message.reply_text('https://malangkab.bps.go.id/subject/10/pertambangan.html#subjekViewTab3 \n----------------\nKlik atau ketikkan /menu untuk kembali ke halaman menu')
    elif 'pp 6' in text_diterima:
        await update.message.reply_text('https://malangkab.bps.go.id/subject/24/peternakan.html#subjekViewTab3 \n----------------\nKlik atau ketikkan /menu untuk kembali ke halaman menu')
    elif 'pp 7' in text_diterima:
        await update.message.reply_text('https://malangkab.bps.go.id/subject/53/tanaman-pangan.html#subjekViewTab3 \n----------------\nKlik atau ketikkan /menu untuk kembali ke halaman menu')
#-----------------

#content command = seluruh operasi rooting akan berjalan disini
async def content_command(update:Update, context: ContextTypes.DEFAULT_TYPE):
    text_diterima: str = update.message.text.lower()

    if 'bps 1' in text_diterima:
        await pst_menu(update)
    elif 'bps 2' in text_diterima:
        await update.message.reply_text('Selamat Datang! \nPanduan Konsultasi Statistik Online & Offline 📲 \n----------------\nPilih Layanan Konsultasi : \n1. Standar Pelayanan Rekomendasi Kegiatan Statistik Sektoral  \n2. Standar Pelayanan Perpustakaan  \n3. Standar Pelayanan Konsultasi Data Statistik  \n4. Standar Pelayanan Penjualan Produk BPS  \n5 Daftar Jenis & Tarif Penerimaan Negara Bukan Pajak BPS  \n----------------\nUntuk memilih, silahkan ketik dengan format berikut : /ks (pilihan anda)\n Contoh : /ks 1')
        await konsultasi_statistik(update, context)
    elif 'bps 3' in text_diterima:
        await data_statistik(update)
    elif 'bps 4' in text_diterima:
        await pojok_statistik(update)
    elif 'bps 5' in text_diterima:
        await saran_pengaduan(update)
    elif 'bps sk' in text_diterima:
        await update.message.reply_text('Selamat Datang! \nSosial dan Kependudukan 👨‍👩‍👧‍👦 \n----------------\nPilih Layanan Informasi : \n1. Agama\n2. Gender\n3. Geografi\n4. Iklim\n5. Indeks Pembangunan Manusia\n6. Kemiskinan dan Ketimpangan \n7. Kependudukan\n8. Kesehatan\n9. Konsumsi dan Pengeluaran\n10. Lingkungan Hidup\n11. Pemerintahan\n12. Pendidikan\n13. Perumahan\n14. Politik dan Keamanan\n15. Sosial Budaya\n16. Tenaga Kerja\n----------------\nUntuk memilih, silahkan ketik dengan format berikut : /sk (pilihan anda)\n Contoh : /sk 1')
        await sosial_kependudukan(update, context)
    elif 'bps ep' in text_diterima:
        await update.message.reply_text('Selamat Datang! \nEkonomi dan Perdagangan      \n----------------\nPilih Layanan Informasi : \n1. Ekspor-Impor\n2. Energi\n3. Harga Eceran\n4. Harga Produsen\n5. Industri\n6. Inflasi\n7. Keuangan\n8. Komunikasi\n9. Pariwisata\n10. Produk Domestik Regional Bruto\n11. Transportasi\n12. Upah Buruh\n----------------\nUntuk memilih, silahkan ketik dengan format berikut : /ep (pilihan anda)\nContoh : /ep 1')
        await ekonomi_perdagangan(update, context)
    elif 'bps pp' in text_diterima:
        await update.message.reply_text('Selamat Datang! \nEkonomi dan Perdagangan      \n----------------\nPilih Layanan Informasi : \n1 Holtikultura\n2. Kehutanan\n3. Perikanan\n4. Perkebunan\n5. Pertambangan\n6. Peternakan\n7. Tanaman Pangan\n----------------\nUntuk memilih, silahkan ketik dengan format berikut : /pp (pilihan anda)\nContoh : /pp 1')
        await pertanian_pertambangan(update, context)
    else:
        await update.message.reply_text('Pilihan tidak ada / valid. Silahkan ketikkan kembali pilihan anda (CONTENT COMMAND)')

if __name__ == '__main__':
    print('BOT STARTED!!')
    application = Application.builder().token(TOKEN).build()

    #main_command
    application.add_handler(CommandHandler('start', start_command))
    application.add_handler(CommandHandler('menu', dashboard_command))
    application.add_handler(CommandHandler('bps', content_command))

    #content_command
    application.add_handler(CommandHandler('ks', konsultasi_statistik))
    application.add_handler(CommandHandler('sk', sosial_kependudukan))
    application.add_handler(CommandHandler('ep', ekonomi_perdagangan))
    application.add_handler(CommandHandler('pp', pertanian_pertambangan))

    #error message
    application.add_handler(MessageHandler(filters.ALL, error))

    # Pooling
    print('START POOLING....')
    application.run_polling(poll_interval=1)