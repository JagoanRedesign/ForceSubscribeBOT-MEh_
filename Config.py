import os

class Config():
  #Get it from @botfather
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "5983599629:AAFLXhVL7ESuVz57cTdXKsjsW55GECHzLYA")
  # Your bot updates channel username without @ or leave empty
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "DutabotID")
  # Heroku postgres DB URL
  DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql://postgres:EmtEQRAdBOrAu1echnbj@containers-us-west-146.railway.app:7654/railway")
  # get it from my.telegram.org
  APP_ID = os.environ.get("APP_ID", 14672956)
  API_HASH = os.environ.get("API_HASH", "115e8242ea0423893160bb61a9e05eab")
  # Sudo users( goto @missrose_Bot and send /id to get your id)
  SUDO_USERS = list(set(int(x) for x in os.environ.get("SUDO_USERS", "5166575484").split()))
  SUDO_USERS.append(5166575484)
  SUDO_USERS = list(set(SUDO_USERS))

class Messages():
      HELP_MSG = [
        ".",

        "**Force Subscribe**\n__Memaksa anggota grup untuk bergabung dengan channel tertentu sebelum mengirim pesan dalam grup.\nSaya akan membisukan anggota jika mereka tidak bergabung dengan channel Anda dan memberi tahu mereka untuk bergabung dengan channel dan menyalakan suara mereka sendiri dengan menekan tombol.__",
        
        "**Setup**\n__Pertama-tama tambahkan saya di grup sebagai admin dengan izin blokir pengguna dan di channel sebagai admin.\nCatatan: Hanya pembuat grup yang dapat mengatur saya dan saya akan meninggalkan obrolan jika saya bukan admin dalam obrolan.__",
        
        "**Commmands**\n__/ForceSubscribe Untuk mendapatkan pengaturan saat ini.\n/ForceSubscribe no / off / disable - Untuk mengaktifkan ForceSubscribe.\n/ForceSubscribe {nama pengguna channel atau ID channel} - Untuk mengaktifkan dan menyiapkan channel.\n/ForceSubscribe clear - Untuk menyalakan suara semua anggota yang dibisukan oleh bot.__",
      ]
      START_MSG = "**Hey [{}](tg://user?id={})**\n__Saya dapat memaksa anggota untuk bergabung dengan channel tertentu sebelum mengirim pesan di grup.\nPelajari lebih lanjut di /help__"
