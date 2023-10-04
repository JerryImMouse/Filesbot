class Text:
    greet = "Привет {name}, я бот созданный для хранения всех конспектов и прочих данных из колледжа КИнЭУ."
    menu = "📖Главное меню"
    uploaded = "Запись внесена в базу данных."
    failed_to_upload = "Запись не была внесена.\n\nВозможные причины:\n1) Заголовок, который вы пытаетесь ввести уже существует в базе.\n\n2) Внутренняя ошибка, в таком случае обратитесь к моему разработчику(Discord: jerryimmouse)"
    not_found = "Под таким заголовком нет ни одного текста."
    choose_title_get = "Выберите заголовок: "
    choose_title_upload = "Впишите заголовок и нужный текст разделив их с помощью (~)"
    insert_text = "Вставьте текст."
    info = "Привет {name}, я бот созданный для хранения всех конспектов и прочих данных из колледжа КИнЭУ.\n\nВ мой функционал входит:\n\n1) Возможность сохранять различные конспекты и ответы к экзаменам в текстовом виде, присваивая им заголовки.\n\n2)Выдавать внесенные в базу данных текста, используя заголовок.\n\n3) Также я могу предоставить информацию о том, как я был создан и GitHub моего разработчика.\n\nС самого начала у вас нет доступа к удалению и записи в базу данных каких либо текстов, за доступом обратитесь в Discord моего разработчика - jerryimmouse. :D"
    titles_list = "Список заголовков: "
    guide = "Значит все же интересно?\nЯ был написан на языке Python, при помощи библиотеки aiogram 3.\nТакже в меня включены такие вещи как SQL база данных, для функционирования с ней я использую sqlite3.\nМеня написали используя информацию с сайтов:\n\nИнформация о библиотеке aiogram 3.\nhttps://mastergroosha.github.io/aiogram-3-guide/ \n\nПомощь в устранении ошибок в коде\nhttps://stackoverflow.com/ \n\nИнформация о библиотеке sqlite3.\nhttps://metanit.com/sql/sqlite/ \n\nПрограмма для просмотра баз данных.\nhttps://sqlitebrowser.org/ \n\nВсё это очень помогло моему создателю в моем написании. Данный список будет пополняться по мере моей разработки.\n\nЕсли вы хотите изучить мои внутренности, то перейдите по ссылке на GitHub моего разработчика и найдите там репозиторий со мной."
    canceled = "Действие отменено."
    crit_delete_error = "Во время удаления произошла ошибка.\n\nНапишите в Discord моему разработчику - jerryimmouse."
    deleted = "Успешно удалено."



    log_started = "Bot started with user: {user_id}/{username}"
    log_unknown_message = "Unknown message deleted. It contained: {message}. UserID/Name - {userid}/{username}"
    log_canceled = "Move canceled by: {userid}/{username}"
    log_got = "Text GOT from DB with title: {title}. UserID/Name - {userid}/{username}"
    log_upload = "Text UPLOADED TO database with title: {title}. UserID/Name - {userid}/{username}"
    log_deleted = "Text DELETED from DB with title: {title}. UserID/Name - {userid}/{username}"