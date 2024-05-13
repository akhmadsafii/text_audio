from gtts import gTTS
import pyttsx3
import os

mytext = "Di sudut kota kecil Magelang, Jawa Tengah, terdapat sebuah perumahan sederhana yang menjadi tempat tinggal bagi seorang pemuda bernama Akhmad Safi'i. Akhmad, seorang pemuda yang penuh semangat dan berbakat di bidang teknologi, telah lama bermimpi untuk membawa perubahan positif melalui dunia digital. Setelah menamatkan pendidikan tingginya di salah satu perguruan tinggi di daerah tersebut, Akhmad Safi'i mendapatkan kesempatan pertamanya di dunia kerja di sebuah perusahaan IT lokal yang berkembang pesat, bernama Dharmasatyanusantara. Dengan hati yang berdebar-debar, dia memasuki dunia kerja dengan semangat yang membara. Bertugas sebagai seorang web developer, Akhmad merasa seperti terdampar di dunia yang baru dan menantang. Namun, dengan tekad dan kerja keras, dia mampu menaklukkan tantangan demi tantangan yang muncul. Selama 7 bulan terakhir, dia telah belajar banyak hal baru, mulai dari menangani kode-kode kompleks hingga menyelesaikan proyek-proyek yang menantang. Meskipun kadang-kadang dia merasa putus asa atau ragu akan kemampuannya, Akhmad tidak pernah menyerah. Dia melihat setiap rintangan sebagai kesempatan untuk tumbuh dan berkembang lebih jauh. Alamat Akhmad di Ngaropoh, Magelang, bukan hanya sekadar lokasi tempat tinggal, tetapi juga menjadi sumber inspirasi bagi dirinya. Di rumah sederhana itu, dia menemukan ketenangan dan kenyamanan setelah seharian bekerja keras. Hari ini, Akhmad Safi'i bukanlah sekadar seorang web developer. Dia adalah contoh nyata dari pemuda yang bersemangat, penuh dedikasi, dan siap menghadapi segala tantangan. Dengan impian besar dan harapan tinggi, dia terus melangkah maju, berusaha keras untuk mewujudkan cita-citanya: menjadi seorang profesional IT yang sukses dan memberikan dampak positif bagi masyarakat di sekitarnya! Di sudut kota kecil Magelang, Jawa Tengah, terdapat sebuah perumahan sederhana yang menjadi tempat tinggal bagi seorang pemuda bernama Akhmad Safi'i. Akhmad, seorang pemuda yang penuh semangat dan berbakat di bidang teknologi, telah lama bermimpi untuk membawa perubahan positif melalui dunia digital. Setelah menamatkan pendidikan tingginya di salah satu perguruan tinggi di daerah tersebut, Akhmad Safi'i mendapatkan kesempatan pertamanya di dunia kerja di sebuah perusahaan IT lokal yang berkembang pesat, bernama Dharmasatyanusantara. Dengan hati yang berdebar-debar, dia memasuki dunia kerja dengan semangat yang membara. Bertugas sebagai seorang web developer, Akhmad merasa seperti terdampar di dunia yang baru dan menantang. Namun, dengan tekad dan kerja keras, dia mampu menaklukkan tantangan demi tantangan yang muncul. Selama 7 bulan terakhir, dia telah belajar banyak hal baru, mulai dari menangani kode-kode kompleks hingga menyelesaikan proyek-proyek yang menantang. Meskipun kadang-kadang dia merasa putus asa atau ragu akan kemampuannya, Akhmad tidak pernah menyerah. Dia melihat setiap rintangan sebagai kesempatan untuk tumbuh dan berkembang lebih jauh. Alamat Akhmad di Ngaropoh, Magelang, bukan hanya sekadar lokasi tempat tinggal, tetapi juga menjadi sumber inspirasi bagi dirinya. Di rumah sederhana itu, dia menemukan ketenangan dan kenyamanan setelah seharian bekerja keras."
language = 'id'

myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("welcome.mp3")

engine = pyttsx3.init()

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)

engine.say("Di sudut kota kecil Magelang, Jawa Tengah.")
engine.runAndWait()

os.system("start welcome.mp3")
