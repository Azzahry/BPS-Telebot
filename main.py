from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "7139442435:AAHuWz7btk8hz_GG2vXcL7bEO4HtUY2ObQI"
USERNAME_BOT = "BPSKABMALANG_bot"


async def start_command(update:Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Selamat datang😊.\nSaya adalah chat bot BPS. Silahkan ikuti panduan berikut untuk berinteraksi dengan chatbot. Klik /panduan')

async def help_command(update:Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Selamat Datang di BPS Kab Malang')

async def menu_command(update:Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_photo('image/logo-or-header/bps-logo.jpg')
    await update.message.reply_text('Selamat Datang😊 \nChatbot BPS Kabupaten Malang\n-------------------------------------------------------\nPilih Layanan Informasi : \n1. Pusat Statistik Terpadu (PST) Online \n2. Panduan Konsultasi Statistik \n3. Visualisasi Data Statistik \n4. Pojok Statistik\n Untuk memilih, gunakan ketikkan format berikut: /bps 1')

async def content_command(update:Update, context: ContextTypes.DEFAULT_TYPE):
    text_diterima: str = update.message.text
    text_diterima.lower()
    #main menu
    if 'bps 1' in text_diterima:
        await update.message.reply_photo('image/logo-or-header/logo-pst.png')
        await update.message.reply_text('Selamat Datang! \nPelayanan Statistik Terpadu (PST) Online 📲 \n-------------------------------------------------------\nBerikut link website seputar PST Online : \n• Keluar [ex]')
    elif 'bps 2' in text_diterima:
        await update.message.reply_photo('image/logo-or-header/statistics-consultan.jpg')
        await update.message.reply_text("Selamat Datang! \nPanduan Konsultasi Statistik Online & Offline 📲 \n-------------------------------------------------------\nPilih Layanan Konsultasi : \n• Standar Pelayanan Rekomendasi Kegiatan Statistik Sektoral [k1]  \n• Standar Pelayanan Perpustakaan [k2] \n• Standar Pelayanan Konsultasi Data Statistik [k3] \n• Standar Pelayanan Penjualan Produk BPS [k4] \n• Daftar Jenis & Tarif Penerimaan Negara Bukan Pajak BPS [k5] \n• Keluar [ex]")
    elif 'bps 3' in text_diterima:
        await update.message.reply_photo('image/logo-or-header/statistics-header.jpg')
        await update.message.reply_text('Selamat Datang! \nVisualisasi Data Statistik 📊 \n\nVisualisasi Data Statistik merupakan layanan informasi mengenai pendataan BPS Kabupaten Malang berupa visual \n-------------------------------------------------------\nPilih Layanan Informasi : \n• Sosial dan kependudukan [sk] \n• Ekonomi dan Perdagangan [ep] \n• Pertanian dan Pertambangan [pp] \n• Keluar [ex]')
    elif 'bps 4' in text_diterima:
        await update.message.reply_photo('image/logo-or-header/pojokstatistik.png')
        await update.message.reply_text('Selamat Datang! \nLayanan Pojok Statistik 📊 \n-------------------------------------------------------\nSilahkan hubungi nomor : \n+62 896-5499-3852 \n• Keluar [ex]')
    #konsul option
    if 'bps k1' in text_diterima:
        await update.message.reply_photo('image/logo-or-header/konsul-1.png')
    elif 'bps k2' in text_diterima:
        await update.message.reply_photo('image/logo-or-header/konsul-2.png')
    elif 'bps k3' in text_diterima:
            await update.message.reply_photo('image/logo-or-header/konsul-3.png')
    elif 'bps k4' in text_diterima:
        await update.message.reply_photo('image/logo-or-header/konsul-4.png')
    elif 'bps k5' in text_diterima:
        await update.message.reply_photo('image/logo-or-header/konsul-5.png')
    #visualisasi option
    if 'bps sk' in text_diterima:
        await update.message.reply_text('Selamat Datang! \nSosial dan Kependudukan 👨‍👩‍👧‍👦 \n-------------------------------------------------------\nPilih Layanan Informasi : \n• Agama [ag] \n• Gender [gd] \n• Geografi [gf] \n• Keluar [ex]')
    elif 'bps ep' in text_diterima:
        await update.message.reply_text('Selamat Datang! \nEkonomi dan Perdagangan 💵 \n-------------------------------------------------------\nPilih Layanan Informasi : \n• Ekspor-Impor \n• Energi \n• Harga Eceran \n• Keluar [ex]')
    elif 'bps pp' in text_diterima:
        await update.message.reply_text('Selamat Datang! \nPertanian dan Pertambangan 🌱 \n-------------------------------------------------------\nPilih Layanan Informasi : \n• Hortikultura \n• Kehutanan \n• Perikanan \n• Keluar [ex]')
    elif 'bps ag' in text_diterima:
        await update.message.reply_photo('image/statistik/sosial-dan-kependudukan/agama/Banyaknya Pondok Pesantren Menurut Kecamatan 2018-2020.png')
        await update.message.reply_photo('image/statistik/sosial-dan-kependudukan/agama/berangkat-haji-2011-2019.png')
    
    
    return await update.message.reply_text('Pilihan tidak ada / valid. Silahkan ketikkan kembali pilihan anda')

# async def konsultasi(update:Update, context:ContextTypes.DEFAULT_TYPE):
#     text_diterima: str = update.message.text
#     text_diterima.lower()
#     if 'bps k1' in text_diterima:
#         await update.message.reply_photo('image/logo-or-header/konsul-1.png')
#     elif 'bps k2' in text_diterima:
#         await update.message.reply_photo('image/logo-or-header/konsul-2.png')
#     elif 'bps k3' in text_diterima:
#             await update.message.reply_photo('image/logo-or-header/konsul-3.png')
#     elif 'bps k4' in text_diterima:
#         await update.message.reply_photo('image/logo-or-header/konsul-4.png')
#     elif 'bps k5' in text_diterima:
#         await update.message.reply_photo('image/logo-or-header/konsul-5.png')
#     else:
#         menu_command()

async def panduan_command(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Untuk mengakses menu pada chatbot ini, anda bisa mengetikkan /menu atau mengklik tombol menu di pojok kiri bawah')

async def error(update:Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'error : {context.error}')

if __name__ == '__main__':
    print('BOT STARTED!!')
    application = Application.builder().token(TOKEN).build()

    #command
    application.add_handler(CommandHandler('start', start_command))
    application.add_handler(CommandHandler('menu', menu_command))
    application.add_handler(CommandHandler('panduan', panduan_command))
    application.add_handler(CommandHandler('bps', content_command))
    # application.add_handler(CommandHandler('ks', konsultasi))
    application.add_handler(CommandHandler('help', help_command))

    application.add_handler(MessageHandler(filters.ALL, error))

    # Pooling
    print('START POOLING....')
    application.run_polling(poll_interval=1)