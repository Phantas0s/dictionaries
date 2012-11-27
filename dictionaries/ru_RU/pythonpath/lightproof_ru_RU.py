# -*- encoding: UTF-8 -*-
dic = [[u'(?iu)(?<![-\\w\u2013.,\xad])\\b[Ff][Oo][Oo]\\b(?![-\\w\u2013\xad])', u'bar', u'test', False], [u'(?iu)(?<![-\\w\u2013.,\xad]) ([.?!,:;)\u201d]($| ))(?![-\\w\u2013\xad])', u'\\1', u'\u041b\u0438\u0448\u043d\u0438\u0439 \u043f\u0440\u043e\u0431\u0435\u043b \u043f\u0435\u0440\u0435\u0434 \u0437\u043d\u0430\u043a\u043e\u043c \u043f\u0443\u043d\u043a\u0442\u0443\u0430\u0446\u0438\u0438.', u'option(LOCALE,"space")'], [u'(?iu)(?<![-\\w\u2013.,\xad])([(\u201c]) (?![-\\w\u2013\xad])', u'\\1', u'\u041b\u0438\u0448\u043d\u0438\u0439 \u043f\u0440\u043e\u0431\u0435\u043b \u043f\u043e\u0441\u043b\u0435 \u0437\u043d\u0430\u043a\u0430 \u043f\u0443\u043d\u043a\u0442\u0443\u0430\u0446\u0438\u0438.', u'option(LOCALE,"space")'], [u'(?iu)(?<![-\\w\u2013.,\xad])(?P<Abc_1>[a-zA-ZA-Z\u0430-\u044f\u0410-\u042f\u0410-\u042f]+)(?P<punct_1>[?!,:;%\u2030\u2031\u02da\u201c\u201d\u2018\u201e])(?P<Abc_2>[a-zA-ZA-Z\u0430-\u044f\u0410-\u042f\u0410-\u042f]+)(?![-\\w\u2013\xad])', u'\\g<Abc_1>\\g<punct_1> \\g<Abc_2>', u'\u041f\u0440\u043e\u043f\u0443\u0449\u0435\u043d \u043f\u0440\u043e\u0431\u0435\u043b?', u'option(LOCALE,"space")'], [u'(?iu)(?<![-\\w\u2013.,\xad])(?P<abc_1>[a-zA-Z\u0430-\u044f\u0410-\u042f]+)[.](?P<ABC_1>[A-Z\u0410-\u042f]+)(?![-\\w\u2013\xad])', u'\\g<abc_1>. \\g<ABC_1>', u'\u041f\u0440\u043e\u043f\u0443\u0449\u0435\u043d \u043f\u0440\u043e\u0431\u0435\u043b?', u'option(LOCALE,"space")'], [u'(?iu)(?<![-\\w\u2013.,\xad])[.]{3}(?![-\\w\u2013\xad])', u'\u2026', u'\u0421\u0438\u043c\u0432\u043e\u043b \u0442\u0440\u043e\u0435\u0442\u043e\u0447\u0438\u044f.', u'option(LOCALE,"typographica")'], [u'(?iu)(?<![-\\w\u2013.,\xad])(\\d+)[Xx](\\d+)(?![-\\w\u2013\xad])', u'\\1\xd7\\2', u'\u0417\u043d\u0430\u043a \u0443\u043c\u043d\u043e\u0436\u0435\u043d\u0438\u044f.', u'option(LOCALE,"typographica")'], [u'(?iu)((?<=[!?.] )|^)[-\u2014] (?![-\\w\u2013\xad])', u'\u2013 ', u'\u0417\u0430\u043c\u0435\u043d\u0438\u0442\u044c \u043d\u0430 \u0442\u0438\u0440\u0435 (n-dash)?', u'option(LOCALE,"typographica")'], [u'(?iu)(?<![-\\w\u2013.,\xad]) [-\u2014]([ ,;])(?![-\\w\u2013\xad])', u' \u2013\\1', u'\u0417\u0430\u043c\u0435\u043d\u0438\u0442\u044c \u043d\u0430 \u0442\u0438\u0440\u0435 (n-dash)?', u'option(LOCALE,"typographica")'], [u'(?iu)(?<![-\\w\u2013.,\xad])[,]{2}(?![-\\w\u2013\xad])', u',', u'\u0414\u0432\u0435 \u0437\u0430\u043f\u044f\u0442\u044b\u0435 \u043f\u043e\u0434\u0440\u044f\u0434.', u'option(LOCALE,"comma")'], [u'(?iu)(?<![-\\w\u2013.,\xad])[ ](?P<abbr_1>[\u0420\u0440][\u0423\u0443][\u0411\u0431]|[\u041a\u043a][\u041e\u043e][\u041f\u043f]|[\u0413\u0433][\u0420\u0440][\u041d\u043d]|[\u0422\u0442][\u042b\u044b][\u0421\u0441]|[\u0423\u0443][\u041b\u043b]|[\u041a\u043a][\u0412\u0432]|[\u041f\u043f][\u041e\u043e][\u0421\u0441]|[\u0421\u0441][\u0422\u0442]|[\u041f\u043f][\u0420\u0440]|[\u041f\u043f][\u0420\u0440][\u041e\u043e][\u0421\u0441][\u041f\u043f]|[\u0415\u0435][\u0414\u0434]|[\u042d\u044d][\u041a\u043a][\u0417\u0437]|[\u0422\u0442][\u0415\u0435][\u041b\u043b]|[\u0418\u0438][\u0421\u0441][\u041f\u043f])[ ](?![-\\w\u2013\xad])', u' \\g<abbr_1>. ', u'\u0422\u043e\u0447\u043a\u0430 \u043f\u043e\u0441\u043b\u0435 \u0441\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u0438\u0439.', u'option(LOCALE,"abbreviation")'], [u'(?iu)(?<![-\\w\u2013.,\xad])(^|\\b|(?P<punct_1>[?!,:;%\u2030\u2031\u02da\u201c\u201d\u2018\u201e])|[.]) {2,3}(\\b|$)(?![-\\w\u2013\xad])', u'\\1 ', u'\u041b\u0438\u0448\u043d\u0438\u0439 \u043f\u0440\u043e\u0431\u0435\u043b.', u'option(LOCALE,"space")'], [u'(?iu)(?<![-\\w\u2013.,\xad])\\"(\\w[^\\"\u201c\u201d]*[\\w.?!,])\\"(?![-\\w\u2013\xad])', u'\xab\\1\xbb\\n\u201e\\1\u201d\\n\u201c\\1\u201d', u'\u041a\u0430\u0432\u044b\u0447\u043a\u0438.', u'option(LOCALE,"quotation")'], [u"(?iu)(?<![-\\w\u2013.,\xad])\\B'(\\w[^']*[\\w.?!,])'\\B(?![-\\w\u2013\xad])", u'\u2018\\1\u2019', u'\u041a\u0430\u0432\u044b\u0447\u043a\u0438.', u'option(LOCALE,"quotation")'], [u"(?iu)(?<![-\\w\u2013.,\xad])(?iu)(?P<Abc_1>[a-zA-ZA-Z\u0430-\u044f\u0410-\u042f\u0410-\u042f]+)'(?P<w_1>\\w*)(?![-\\w\u2013\xad])", u'\\g<Abc_1>\u2019\\g<w_1>', u'\u0410\u043f\u043e\u0441\u0442\u0440\u043e\u0444.', u'option(LOCALE,"quotation")'], [u'(?iu)(?<![-\\w\u2013.,\xad])(?P<abc_1>[a-zA-Z\u0430-\u044f\u0410-\u042f]+)[ ][\u0410\u0430][ ](?![-\\w\u2013\xad])', u'\\g<abc_1>, \u0430 ', u'\u041f\u0440\u043e\u043f\u0443\u0449\u0435\u043d\u0430 \u0437\u0430\u043f\u044f\u0442\u0430\u044f \u043f\u0435\u0440\u0435\u0434 \u0430.', u'option(LOCALE,"comma")'], [u'(?iu)(?<![-\\w\u2013.,\xad])(?P<abc_1>[a-zA-Z\u0430-\u044f\u0410-\u042f]+)[ ][\u041d\u043d][\u041e\u043e][ ](?![-\\w\u2013\xad])', u'\\g<abc_1>, \u043d\u043e ', u'\u041f\u0440\u043e\u043f\u0443\u0449\u0435\u043d\u0430 \u0437\u0430\u043f\u044f\u0442\u0430\u044f \u043f\u0435\u0440\u0435\u0434 \u043d\u043e.', u'option(LOCALE,"comma")'], [u'(?iu)(?<![-\\w\u2013.,\xad])(?P<abc_1>[a-zA-Z\u0430-\u044f\u0410-\u042f]+), (?P<novvod_1>[\u0410\u0430][\u0412\u0432][\u041e\u043e][\u0421\u0441][\u042c\u044c]|[\u0411\u0431][\u0423\u0443][\u041a\u043a][\u0412\u0432][\u0410\u0430][\u041b\u043b][\u042c\u044c][\u041d\u043d][\u041e\u043e]|[\u0411\u0431][\u0423\u0443][\u0414\u0434][\u0422\u0442][\u041e\u043e]|[\u0412\u0432][\u0414\u0434][\u041e\u043e][\u0411\u0431][\u0410\u0430][\u0412\u0432][\u041e\u043e][\u041a\u043a]|[\u0412\u0432][\u0414\u0434][\u0420\u0440][\u0423\u0443][\u0413\u0433]|[\u0412\u0432][\u0415\u0435][\u0414\u0434][\u042c\u044c]|[\u0412\u0432][\u041e\u043e][\u0422\u0442]|[\u0414\u0434][\u0410\u0430][\u0416\u0436][\u0415\u0435]|[\u0418\u0438][\u0421\u0441][\u041a\u043a][\u041b\u043b][\u042e\u044e][\u0427\u0447][\u0418\u0438][\u0422\u0442][\u0415\u0435][\u041b\u043b][\u042c\u044c][\u041d\u043d][\u041e\u043e]|[\u0418\u0438][\u041c\u043c][\u0415\u0435][\u041d\u043d][\u041d\u043d][\u041e\u043e]|[\u041d\u043d][\u0415\u0435][\u0411\u0431][\u041e\u043e][\u0421\u0441][\u042c\u044c]|[\u041f\u043f][\u0420\u0440][\u0418\u0438][\u0411\u0431][\u041b\u043b][\u0418\u0438][\u0417\u0437][\u0418\u0438][\u0422\u0442][\u0415\u0435][\u041b\u043b][\u042c\u044c][\u041d\u043d][\u041e\u043e]|[\u041f\u043f][\u0420\u0440][\u0418\u0438][\u041c\u043c][\u0415\u0435][\u0420\u0440][\u041d\u043d][\u041e\u043e]|[\u041f\u043f][\u0420\u0440][\u0418\u0438][\u0422\u0442][\u041e\u043e][\u041c\u043c]|[\u041f\u043f][\u041e\u043e][\u0427\u0447][\u0422\u0442][\u0418\u0438]|[\u041f\u043f][\u041e\u043e][\u042d\u044d][\u0422\u0442][\u041e\u043e][\u041c\u043c][\u0423\u0443]|[\u041f\u043f][\u0420\u0440][\u041e\u043e][\u0421\u0441][\u0422\u0442][\u041e\u043e]|[\u0420\u0440][\u0415\u0435][\u0428\u0448][\u0418\u0438][\u0422\u0442][\u0415\u0435][\u041b\u043b][\u042c\u044c][\u041d\u043d][\u041e\u043e]|[\u0421\u0441][\u041b\u043b][\u041e\u043e][\u0412\u0432][\u041d\u043d][\u041e\u043e]|[\u042f\u044f][\u041a\u043a][\u041e\u043e][\u0411\u0431][\u042b\u044b]|[\u0412\u0432] [\u0414\u0434][\u041e\u043e][\u0412\u0432][\u0415\u0435][\u0420\u0440][\u0428\u0448][\u0415\u0435][\u041d\u043d][\u0418\u0438][\u0415\u0435]|[\u0412\u0432] [\u041a\u043a][\u041e\u043e][\u041d\u043d][\u0415\u0435][\u0427\u0447][\u041d\u043d][\u041e\u043e][\u041c\u043c] [\u0421\u0441][\u0427\u0447][\u0415\u0435][\u0422\u0442][\u0415\u0435]|[\u0412\u0432][\u0420\u0440][\u042f\u044f][\u0414\u0434] [\u041b\u043b][\u0418\u0438]|[\u0412\u0432][\u0421\u0441][\u0415\u0435]-[\u0422\u0442][\u0410\u0430][\u041a\u043a][\u0418\u0438]|[\u041a\u043a][\u0410\u0430][\u041a\u043a] [\u0411\u0431][\u0423\u0443][\u0414\u0434][\u0422\u0442][\u041e\u043e]|[\u041a\u043a][\u0410\u0430][\u041a\u043a] [\u0411\u0431][\u042b\u044b]|[\u041a\u043a][\u0410\u0430][\u041a\u043a] [\u0420\u0440][\u0410\u0430][\u0417\u0437]|[\u041a\u043a] [\u0422\u0442][\u041e\u043e][\u041c\u043c][\u0423\u0443] [\u0416\u0436][\u0415\u0435]|[\u041c\u043c][\u0415\u0435][\u0416\u0436][\u0414\u0434][\u0423\u0443] [\u0422\u0442][\u0415\u0435][\u041c\u043c]|[\u041f\u043f][\u041e\u043e] [\u041f\u043f][\u0420\u0440][\u0415\u0435][\u0414\u0434][\u041b\u043b][\u041e\u043e][\u0416\u0436][\u0415\u0435][\u041d\u043d][\u0418\u0438][\u042e\u044e]|[\u041f\u043f][\u041e\u043e] [\u041f\u043f][\u041e\u043e][\u0421\u0441][\u0422\u0442][\u0410\u0430][\u041d\u043d][\u041e\u043e][\u0412\u0432][\u041b\u043b][\u0415\u0435][\u041d\u043d][\u0418\u0438][\u042e\u044e]|[\u041f\u043f][\u041e\u043e] [\u0420\u0440][\u0415\u0435][\u0428\u0448][\u0415\u0435][\u041d\u043d][\u0418\u0438][\u042e\u044e]),(?![-\\w\u2013\xad])', u'\\g<abc_1> \\g<novvod_1>', u'\u0421\u043b\u043e\u0432\u0430, \u043d\u0435 \u044f\u0432\u043b\u044f\u044e\u0449\u0438\u0435\u0441\u044f \u0432\u0432\u043e\u0434\u043d\u044b\u043c\u0438.', u'option(LOCALE,"comma")'], [u'(?iu)(?<![-\\w\u2013.,\xad])(?P<abc_1>[a-zA-Z\u0430-\u044f\u0410-\u042f]+) (?P<vvod_1>[\u0418\u0438][\u0422\u0442][\u0410\u0430][\u041a\u043a]|[\u0421\u0441][\u041b\u043b][\u0415\u0435][\u0414\u0434][\u041e\u043e][\u0412\u0432][\u0410\u0430][\u0422\u0442][\u0415\u0435][\u041b\u043b][\u042c\u044c][\u041d\u043d][\u041e\u043e]|[\u0412\u0432][\u041e\u043e]-[\u041f\u043f][\u0415\u0435][\u0420\u0440][\u0412\u0432][\u042b\u044b][\u0425\u0445]|[\u0412\u0432][\u041e\u043e]-[\u0412\u0432][\u0422\u0442][\u041e\u043e][\u0420\u0440][\u042b\u044b][\u0425\u0445]|[\u0412\u0432]-[\u0422\u0442][\u0420\u0440][\u0415\u0435][\u0422\u0442][\u042c\u044c][\u0418\u0438][\u0425\u0445]|[\u0412\u0432]-[\u0427\u0447][\u0415\u0435][\u0422\u0442][\u0412\u0432][\u0415\u0435][\u0420\u0440][\u0422\u0442][\u042b\u044b][\u0425\u0445]|[\u0412\u0432]-[\u041f\u043f][\u042f\u044f][\u0422\u0442][\u042b\u044b][\u0425\u0445]|[\u041f\u043f][\u041e\u043e][\u0416\u0436][\u0410\u0430][\u041b\u043b][\u0423\u0443][\u0419\u0439][\u0421\u0441][\u0422\u0442][\u0410\u0430]|[\u041a\u043a][\u0410\u0430][\u041a\u043a] [\u041d\u043d][\u0410\u0430][\u0420\u0440][\u041e\u043e][\u0427\u0447][\u041d\u043d][\u041e\u043e]|[\u041a\u043a][\u0410\u0430][\u041a\u043a] [\u0418\u0438][\u0421\u0441][\u041a\u043a][\u041b\u043b][\u042e\u044e][\u0427\u0447][\u0415\u0435][\u041d\u043d][\u0418\u0438][\u0415\u0435]|[\u041a\u043a][\u0410\u0430][\u041a\u043a] [\u041f\u043f][\u0420\u0440][\u0410\u0430][\u0412\u0432][\u0418\u0438][\u041b\u043b][\u041e\u043e])(?![-\\w\u2013\xad])', u'\\g<abc_1>, \\g<vvod_1>,', u'\u0421\u043b\u043e\u0432\u0430, \u044f\u0432\u043b\u044f\u044e\u0449\u0438\u0435\u0441\u044f \u0432\u0432\u043e\u0434\u043d\u044b\u043c\u0438, \u0432\u044b\u0434\u0435\u043b\u044f\u044e\u0442\u0441\u044f \u0437\u0430\u043f\u044f\u0442\u044b\u043c\u0438.', u'option(LOCALE,"comma")'], [u'(?iu)(?<![-\\w\u2013.,\xad])\\b[\u041b\u043b][\u041e\u043e][\u0416\u0436][\u0418\u0438][\u0422\u0442][\u042c\u044c]\\b(?![-\\w\u2013\xad])', u'\u043a\u043b\u0430\u0441\u0442\u044c', u'\u041e\u0431\u0449\u0438\u0435 \u043e\u0448\u0438\u0431\u043a\u0438', u'option(LOCALE,"common")'], [u'(?iu)(?<![-\\w\u2013.,\xad])\\b[\u041b\u043b][\u042f\u044f][\u0416\u0436][\u042c\u044c]\\b(?![-\\w\u2013\xad])', u'\u043b\u044f\u0433', u'\u041e\u0431\u0449\u0438\u0435 \u043e\u0448\u0438\u0431\u043a\u0438', u'option(LOCALE,"common")'], [u'(?iu)(?<![-\\w\u2013.,\xad])\\b[\u0415\u0435][\u0425\u0445][\u0410\u0430][\u0419\u0439]\\b(?![-\\w\u2013\xad])', u'\u043f\u043e\u0435\u0437\u0436\u0430\u0439', u'\u041e\u0431\u0449\u0438\u0435 \u043e\u0448\u0438\u0431\u043a\u0438', u'option(LOCALE,"common")'], [u'(?iu)(?<![-\\w\u2013.,\xad])\\b[\u0418\u0438][\u0425\u0445][\u041d\u043d](?P<abc_1>[a-zA-Z\u0430-\u044f\u0410-\u042f]+)\\b(?![-\\w\u2013\xad])', u'\u0438\u0445', u'\u041f\u0440\u0438\u0442\u044f\u0436\u0430\u0442\u0435\u043b\u044c\u043d\u043e\u0435 \u043c\u0435\u0441\u0442\u043e\u0438\u043c\u0435\u043d\u0438\u0435 \u043d\u0435 \u0441\u043a\u043b\u043e\u043d\u044f\u0435\u0442\u0441\u044f', u'option(LOCALE,"common")'], [u'(?iu)(?<![-\\w\u2013.,\xad])[\u0416\u0436][\u042b\u044b](?![-\\w\u2013\xad])', u'\u0436\u0438', u'\u0427\u0435\u0440\u0435\u0437 "\u0438"', u'option(LOCALE,"common")'], [u'(?iu)(?<![-\\w\u2013.,\xad])[\u0428\u0448][\u042b\u044b](?![-\\w\u2013\xad])', u'\u0448\u0438', u'\u0427\u0435\u0440\u0435\u0437 "\u0438"', u'option(LOCALE,"common")'], [u'(?iu)(?<![-\\w\u2013.,\xad])\\b[\u041d\u043d][\u041e\u043e][\u0420\u0440][\u0414\u0434] [\u041e\u043e][\u0421\u0441][\u0422\u0442]\\b(?![-\\w\u2013\xad])', u'\u043d\u043e\u0440\u0434-\u043e\u0441\u0442\\n\u043d\u043e\u0440\u0434\u043e\u0441\u0442', u'\u0414\u0435\u0444\u0438\u0441?', u'option(LOCALE,"hyphen")'], [u'(?iu)(?<![-\\w\u2013.,\xad])\\b[\u041d\u043d][\u041e\u043e][\u0420\u0440][\u0414\u0434] [\u0412\u0432][\u0415\u0435][\u0421\u0441][\u0422\u0442]\\b(?![-\\w\u2013\xad])', u'\u043d\u043e\u0440\u0434-\u0432\u0435\u0441\u0442\\n\u043d\u043e\u0440\u0434\u0432\u0435\u0441\u0442', u'\u0414\u0435\u0444\u0438\u0441?', u'option(LOCALE,"hyphen")'], [u'(?iu)(?<![-\\w\u2013.,\xad])\\b[\u0421\u0441][\u0415\u0435][\u0412\u0432][\u0415\u0435][\u0420\u0440][\u041e\u043e] [\u0417\u0437][\u0410\u0430][\u041f\u043f][\u0410\u0430][\u0414\u0434][\u041d\u043d](?P<abc_1>[a-zA-Z\u0430-\u044f\u0410-\u042f]+)\\b(?![-\\w\u2013\xad])', u'\u0441\u0435\u0432\u0435\u0440\u043e-\u0437\u0430\u043f\u0430\u0434\u043d\\g<abc_1>\\n\u0441\u0435\u0432\u0435\u0440\u043e\u0437\u0430\u043f\u0430\u0434\u043d\\g<abc_1>', u'\u0414\u0435\u0444\u0438\u0441?', u'option(LOCALE,"hyphen")'], [u'(?iu)(?<![-\\w\u2013.,\xad])\\b[\u042e\u044e][\u0413\u0433][\u041e\u043e] [\u0417\u0437][\u0410\u0430][\u041f\u043f][\u0410\u0430][\u0414\u0434][\u041d\u043d](?P<abc_1>[a-zA-Z\u0430-\u044f\u0410-\u042f]+)\\b(?![-\\w\u2013\xad])', u'\u044e\u0433\u043e-\u0437\u0430\u043f\u0430\u0434\u043d\\g<abc_1>\\n\u044e\u0433\u043e\u0437\u0430\u043f\u0430\u0434\u043d\\g<abc_1>', u'\u0414\u0435\u0444\u0438\u0441?', u'option(LOCALE,"hyphen")'], [u'(?iu)(?<![-\\w\u2013.,\xad])\\b[\u0421\u0441][\u0415\u0435][\u0412\u0432][\u0415\u0435][\u0420\u0440][\u041e\u043e] [\u0412\u0432][\u041e\u043e][\u0421\u0441][\u0422\u0442][\u041e\u043e][\u0427\u0447][\u041d\u043d](?P<abc_1>[a-zA-Z\u0430-\u044f\u0410-\u042f]+)\\b(?![-\\w\u2013\xad])', u'\u0441\u0435\u0432\u0435\u0440\u043e-\u0432\u043e\u0441\u0442\u043e\u0447\u043d\\g<abc_1>\\n\u0441\u0435\u0432\u0435\u0440\u043e\u0432\u043e\u0441\u0442\u043e\u0447\u043d\\g<abc_1>', u'\u0414\u0435\u0444\u0438\u0441?', u'option(LOCALE,"hyphen")'], [u'(?iu)(?<![-\\w\u2013.,\xad])\\b[\u042e\u044e][\u0413\u0433][\u041e\u043e] [\u0412\u0432][\u041e\u043e][\u0421\u0441][\u0422\u0442][\u041e\u043e][\u0427\u0447][\u041d\u043d](?P<abc_1>[a-zA-Z\u0430-\u044f\u0410-\u042f]+)\\b(?![-\\w\u2013\xad])', u'\u044e\u0433\u043e-\u0432\u043e\u0441\u0442\u043e\u0447\u043d\\g<abc_1>\\n\u044e\u0433\u043e\u0432\u043e\u0441\u0442\u043e\u0447\u043d\\g<abc_1>', u'\u0414\u0435\u0444\u0438\u0441?', u'option(LOCALE,"hyphen")'], [u'(?iu)(?<![-\\w\u2013.,\xad])\\b(?P<adv1_1>[\u041a\u043a][\u0422\u0442][\u041e\u043e]|[\u0427\u0447][\u0422\u0442][\u041e\u043e]|[\u0413\u0433][\u0414\u0434][\u0415\u0435]|[\u0417\u0437][\u0410\u0430][\u0427\u0447][\u0415\u0435][\u041c\u043c]|[\u041a\u043a][\u041e\u043e][\u0415\u0435]) [\u041d\u043d][\u0418\u0438][\u0411\u0431][\u0423\u0443][\u0414\u0434][\u042c\u044c]\\b(?![-\\w\u2013\xad])', u'\\g<adv1_1>-\u043d\u0438\u0431\u0443\u0434\u044c', u'\u0414\u0435\u0444\u0438\u0441?', u'option(LOCALE,"hyphen")'], [u'(?iu)(?<![-\\w\u2013.,\xad])\\b(?P<adv1_1>[\u041a\u043a][\u0422\u0442][\u041e\u043e]|[\u0427\u0447][\u0422\u0442][\u041e\u043e]|[\u0413\u0433][\u0414\u0434][\u0415\u0435]|[\u0417\u0437][\u0410\u0430][\u0427\u0447][\u0415\u0435][\u041c\u043c]|[\u041a\u043a][\u041e\u043e][\u0415\u0435]) [\u041b\u043b][\u0418\u0438][\u0411\u0431][\u041e\u043e]\\b(?![-\\w\u2013\xad])', u'\\g<adv1_1>-\u043b\u0438\u0431\u043e', u'\u0414\u0435\u0444\u0438\u0441?', u'option(LOCALE,"hyphen")'], [u'(?iu)(?<![-\\w\u2013.,\xad])\\b(?P<adv1_1>[\u041a\u043a][\u0422\u0442][\u041e\u043e]|[\u0427\u0447][\u0422\u0442][\u041e\u043e]|[\u0413\u0433][\u0414\u0434][\u0415\u0435]|[\u0417\u0437][\u0410\u0430][\u0427\u0447][\u0415\u0435][\u041c\u043c]|[\u041a\u043a][\u041e\u043e][\u0415\u0435]) [\u0422\u0442][\u041e\u043e]\\b(?![-\\w\u2013\xad])', u'\\g<adv1_1>-\u0442\u043e', u'\u0414\u0435\u0444\u0438\u0441?', u'option(LOCALE,"hyphen")'], [u'(?iu)(?<![-\\w\u2013.,\xad])\\b[\u0422\u0442][\u041e\u043e][\u0427\u0447][\u042c\u044c] [\u0412\u0432] [\u0422\u0442][\u041e\u043e][\u0427\u0447][\u042c\u044c]\\b(?![-\\w\u2013\xad])', u'\u0442\u043e\u0447\u044c-\u0432-\u0442\u043e\u0447\u044c', u'\u0414\u0435\u0444\u0438\u0441?', u'option(LOCALE,"hyphen")'], [u'(?iu)(?<![-\\w\u2013.,\xad])\\b[\u0418\u0438][\u0417\u0437] [\u0417\u0437][\u0410\u0430]\\b(?![-\\w\u2013\xad])', u'\u0438\u0437-\u0437\u0430', u'\u0414\u0435\u0444\u0438\u0441?', u'option(LOCALE,"hyphen")'], [u'(?iu)(?<![-\\w\u2013.,\xad])\\b[\u0412\u0432][\u0421\u0441][\u0401\u0451] [\u0422\u0442][\u0410\u0430][\u041a\u043a][\u0418\u0438]\\b(?![-\\w\u2013\xad])', u'\u0432\u0441\u0451-\u0442\u0430\u043a\u0438', u'\u0414\u0435\u0444\u0438\u0441?', u'option(LOCALE,"hyphen")'], [u'(?iu)(?<![-\\w\u2013.,\xad])\\b[\u041a\u043a][\u041e\u043e][\u0415\u0435] [\u041a\u043a][\u0422\u0442][\u041e\u043e]\\b(?![-\\w\u2013\xad])', u'\u043a\u043e\u0435-\u043a\u0442\u043e', u'\u0414\u0435\u0444\u0438\u0441?', u'option(LOCALE,"hyphen")'], [u'(?iu)(?<![-\\w\u2013.,\xad])\\b[\u041a\u043a][\u041e\u043e][\u0415\u0435] [\u0427\u0447][\u0422\u0442][\u041e\u043e]\\b(?![-\\w\u2013\xad])', u'\u043a\u043e\u0435-\u0447\u0442\u043e', u'\u0414\u0435\u0444\u0438\u0441?', u'option(LOCALE,"hyphen")'], [u'(?iu)(?<![-\\w\u2013.,\xad])\\b[\u0412\u0432][\u041e\u043e] [\u0427\u0447][\u0422\u0442][\u041e\u043e] [\u0411\u0431][\u042b\u044b] [\u0422\u0442][\u041e\u043e] [\u041d\u043d][Ee] [\u0421\u0441][\u0422\u0442][\u0410\u0430][\u041b\u043b][\u041e\u043e]\\b(?![-\\w\u2013\xad])', u'\u0432\u043e \u0447\u0442\u043e \u0431\u044b \u0442\u043e \u043d\u0438 \u0441\u0442\u0430\u043b\u043e', u'\u0418\u043c\u0435\u043b\u043e\u0441\u044c \u0432\u0432\u0438\u0434\u0443:', u'option(LOCALE,"multiword")'], [u'(?iu)(?<![-\\w\u2013.,\xad])\\b[\u0412\u0432][\u041e\u043e] [\u0427\u0447][\u0422\u0442][\u041e\u043e][\u0411\u0431][\u042b\u044b] [\u0422\u0442][\u041e\u043e] [\u041d\u043d][Ee] [\u0421\u0441][\u0422\u0442][\u0410\u0430][\u041b\u043b][\u041e\u043e]\\b(?![-\\w\u2013\xad])', u'\u0432\u043e \u0447\u0442\u043e \u0431\u044b \u0442\u043e \u043d\u0438 \u0441\u0442\u0430\u043b\u043e', u'\u0418\u043c\u0435\u043b\u043e\u0441\u044c \u0432\u0432\u0438\u0434\u0443:', u'option(LOCALE,"multiword")'], [u'(?iu)(?<![-\\w\u2013.,\xad])\\b[\u0412\u0432][\u041e\u043e] [\u0427\u0447][\u0422\u0442][\u041e\u043e][\u0411\u0431][\u042b\u044b] [\u0422\u0442][\u041e\u043e] [\u041d\u043d][\u0418\u0438] [\u0421\u0441][\u0422\u0442][\u0410\u0430][\u041b\u043b][\u041e\u043e]\\b(?![-\\w\u2013\xad])', u'\u0432\u043e \u0447\u0442\u043e \u0431\u044b \u0442\u043e \u043d\u0438 \u0441\u0442\u0430\u043b\u043e', u'\u0418\u043c\u0435\u043b\u043e\u0441\u044c \u0432\u0432\u0438\u0434\u0443:', u'option(LOCALE,"multiword")'], [u'(?iu)(?<![-\\w\u2013.,\xad])\\b[\u0422\u0442][\u0410\u0430][\u041a\u043a][\u0416\u0436][\u0415\u0435] [\u041a\u043a][\u0410\u0430][\u041a\u043a] [\u0418\u0438]\\b(?![-\\w\u2013\xad])', u'\u0442\u0430\u043a \u0436\u0435 \u043a\u0430\u043a \u0438', u'\u0421\u043b\u043e\u0436\u043d\u044b\u0439 \u0441\u043e\u044e\u0437.', u'option(LOCALE,"multiword")'], [u'(?iu)(?<![-\\w\u2013.,\xad])\\b[\u0412\u0432][\u041e\u043e] [\u0418\u0438][\u0417\u0437][\u0411\u0431][\u0415\u0435][\u0416\u0436][\u0410\u0430][\u041d\u043d][\u0418\u0438][\u0418\u0438]\\b(?![-\\w\u2013\xad])', u'\u0432\u043e \u0438\u0437\u0431\u0435\u0436\u0430\u043d\u0438\u0435', u'\u0421\u043b\u043e\u0436\u043d\u044b\u0439 \u043f\u0440\u0435\u0434\u043b\u043e\u0433.', u'option(LOCALE,"multiword")'], [u'(?iu)(?<![-\\w\u2013.,\xad])\\b[\u0420\u0440][\u0410\u0430][\u0412\u0432][\u041d\u043d][\u041e\u043e][\u041f\u043f][\u0420\u0440][\u0410\u0430][\u0412\u0432][\u041d\u043d][\u042b\u044b] [\u0414\u0434][\u0420\u0440][\u0423\u0443][\u0413\u0433] [\u0414\u0434][\u0420\u0440][\u0423\u0443][\u0413\u0433][\u0423\u0443]\\b(?![-\\w\u2013\xad])', u'\u0440\u0430\u0432\u043d\u043e\u043f\u0440\u0430\u0432\u043d\u044b \u0434\u0440\u0443\u0433 c \u0434\u0440\u0443\u0433\u043e\u043c', u'\u0420\u0430\u0432\u043d\u043e\u043f\u0440\u0430\u0432\u043d\u044b \u0434\u0440\u0443\u0433 c \u0434\u0440\u0443\u0433\u043e\u043c.', u'option(LOCALE,"multiword")'], [u'(?iu)(?<![-\\w\u2013.,\xad])\\b[\u041d\u043d][\u0418\u0438] [\u041a\u043a][\u0422\u0442][\u041e\u043e] [\u0418\u0438][\u041d\u043d][\u041e\u043e][\u0419\u0439] [\u041a\u043a][\u0410\u0430][\u041a\u043a]\\b(?![-\\w\u2013\xad])', u'\u043d\u0435 \u043a\u0442\u043e \u0438\u043d\u043e\u0439, \u043a\u0430\u043a', u'\u041e\u0431\u043e\u0440\u043e\u0442.', u'option(LOCALE,"multiword")'], [u'(?iu)(?<![-\\w\u2013.,\xad])\\b[\u041d\u043d][\u0418\u0438] [\u0427\u0447][\u0422\u0442][\u041e\u043e] [\u0418\u0438][\u041d\u043d][\u041e\u043e][\u0415\u0435] [\u041a\u043a][\u0410\u0430][\u041a\u043a]\\b(?![-\\w\u2013\xad])', u'\u043d\u0435 \u0447\u0442\u043e \u0438\u043d\u043e\u0435, \u043a\u0430\u043a', u'\u041e\u0431\u043e\u0440\u043e\u0442.', u'option(LOCALE,"multiword")'], [u'(?iu)(?<![-\\w\u2013.,\xad])\\b[\u041d\u043d][\u0415\u0435] [\u041a\u043a][\u0422\u0442][\u041e\u043e] [\u0418\u0438][\u041d\u043d][\u041e\u043e][\u0419\u0439] [\u041a\u043a][\u0410\u0430][\u041a\u043a]\\b(?![-\\w\u2013\xad])', u'\u043d\u0435 \u043a\u0442\u043e \u0438\u043d\u043e\u0439, \u043a\u0430\u043a', u'\u041e\u0431\u043e\u0440\u043e\u0442.', u'option(LOCALE,"multiword")'], [u'(?iu)(?<![-\\w\u2013.,\xad])\\b[\u041d\u043d][\u0415\u0435] [\u0427\u0447][\u0422\u0442][\u041e\u043e] [\u0418\u0438][\u041d\u043d][\u041e\u043e][\u0415\u0435] [\u041a\u043a][\u0410\u0430][\u041a\u043a]\\b(?![-\\w\u2013\xad])', u'\u043d\u0435 \u0447\u0442\u043e \u0438\u043d\u043e\u0435, \u043a\u0430\u043a', u'\u041e\u0431\u043e\u0440\u043e\u0442.', u'option(LOCALE,"multiword")'], [u'(?iu)(?<![-\\w\u2013.,\xad])\\b[\u041d\u043d][\u0418\u0438][\u041a\u043a][\u0422\u0442][\u041e\u043e] [\u0418\u0438][\u041d\u043d][\u041e\u043e][\u0419\u0439], [\u041d\u043d][\u0415\u0435]\\b(?![-\\w\u2013\xad])', u'\u043d\u0438\u043a\u0442\u043e \u0438\u043d\u043e\u0439 \u043d\u0435', u'\u041e\u0431\u043e\u0440\u043e\u0442.', u'option(LOCALE,"multiword")'], [u'(?iu)(?<![-\\w\u2013.,\xad])\\b[\u041d\u043d][\u0418\u0438][\u0427\u0447][\u0422\u0442][\u041e\u043e] [\u0418\u0438][\u041d\u043d][\u041e\u043e][\u0415\u0435], [\u041d\u043d][\u0415\u0435]\\b(?![-\\w\u2013\xad])', u'\u043d\u0438\u0447\u0442\u043e \u0438\u043d\u043e\u0435 \u043d\u0435', u'\u041e\u0431\u043e\u0440\u043e\u0442.', u'option(LOCALE,"multiword")'], [u'(?iu)(?<![-\\w\u2013.,\xad])\\b[\u041d\u043d][\u0415\u0435][\u041a\u043a][\u0422\u0442][\u041e\u043e] [\u0418\u0438][\u041d\u043d][\u041e\u043e][\u0419\u0439], [\u041d\u043d][\u0415\u0435]\\b(?![-\\w\u2013\xad])', u'\u043d\u0438\u043a\u0442\u043e \u0438\u043d\u043e\u0439 \u043d\u0435', u'\u041e\u0431\u043e\u0440\u043e\u0442.', u'option(LOCALE,"multiword")'], [u'(?iu)(?<![-\\w\u2013.,\xad])\\b[\u041d\u043d][\u0415\u0435][\u0427\u0447][\u0422\u0442][\u041e\u043e] [\u0418\u0438][\u041d\u043d][\u041e\u043e][\u0415\u0435], [\u041d\u043d][\u0415\u0435]\\b(?![-\\w\u2013\xad])', u'\u043d\u0438\u0447\u0442\u043e \u0438\u043d\u043e\u0435 \u043d\u0435', u'\u041e\u0431\u043e\u0440\u043e\u0442.', u'option(LOCALE,"multiword")'], [u'(?iu)(?<![-\\w\u2013.,\xad])\\b[\u041d\u043d][\u0415\u0435][\u041a\u043a][\u0422\u0442][\u041e\u043e] [\u0418\u0438][\u041d\u043d][\u041e\u043e][\u0419\u0439] [\u041d\u043d][\u0415\u0435]\\b(?![-\\w\u2013\xad])', u'\u043d\u0438\u043a\u0442\u043e \u0438\u043d\u043e\u0439 \u043d\u0435', u'\u041e\u0431\u043e\u0440\u043e\u0442.', u'option(LOCALE,"multiword")'], [u'(?iu)(?<![-\\w\u2013.,\xad])\\b[\u041d\u043d][\u0415\u0435][\u0427\u0447][\u0422\u0442][\u041e\u043e] [\u0418\u0438][\u041d\u043d][\u041e\u043e][\u0415\u0435] [\u041d\u043d][\u0415\u0435]\\b(?![-\\w\u2013\xad])', u'\u043d\u0438\u0447\u0442\u043e \u0438\u043d\u043e\u0435 \u043d\u0435', u'\u041e\u0431\u043e\u0440\u043e\u0442.', u'option(LOCALE,"multiword")'], [u'(?iu)(?<![-\\w\u2013.,\xad])\\b[\u041d\u043d][\u0415\u0435] [\u041a\u043a][\u0422\u0442][\u041e\u043e] [\u0418\u0438][\u041d\u043d][\u041e\u043e][\u0419\u0439], [\u041d\u043d][\u0415\u0435]\\b(?![-\\w\u2013\xad])', u'\u043d\u0438\u043a\u0442\u043e \u0438\u043d\u043e\u0439 \u043d\u0435', u'\u041e\u0431\u043e\u0440\u043e\u0442.', u'option(LOCALE,"multiword")'], [u'(?iu)(?<![-\\w\u2013.,\xad])\\b[\u041d\u043d][\u0415\u0435] [\u0427\u0447][\u0422\u0442][\u041e\u043e] [\u0418\u0438][\u041d\u043d][\u041e\u043e][\u0415\u0435], [\u041d\u043d][\u0415\u0435]\\b(?![-\\w\u2013\xad])', u'\u043d\u0438\u0447\u0442\u043e \u0438\u043d\u043e\u0435 \u043d\u0435', u'\u041e\u0431\u043e\u0440\u043e\u0442.', u'option(LOCALE,"multiword")'], [u'(?iu)(?<![-\\w\u2013.,\xad])\\b[\u041d\u043d][\u0415\u0435] [\u041a\u043a][\u0422\u0442][\u041e\u043e] [\u0418\u0438][\u041d\u043d][\u041e\u043e][\u0419\u0439] [\u041d\u043d][\u0415\u0435]\\b(?![-\\w\u2013\xad])', u'\u043d\u0438\u043a\u0442\u043e \u0438\u043d\u043e\u0439 \u043d\u0435', u'\u041e\u0431\u043e\u0440\u043e\u0442.', u'option(LOCALE,"multiword")'], [u'(?iu)(?<![-\\w\u2013.,\xad])\\b[\u041d\u043d][\u0415\u0435] [\u0427\u0447][\u0422\u0442][\u041e\u043e] [\u0418\u0438][\u041d\u043d][\u041e\u043e][\u0415\u0435] [\u041d\u043d][\u0415\u0435]\\b(?![-\\w\u2013\xad])', u'\u043d\u0438\u0447\u0442\u043e \u0438\u043d\u043e\u0435 \u043d\u0435', u'\u041e\u0431\u043e\u0440\u043e\u0442.', u'option(LOCALE,"multiword")'], [u'(?iu)(?<![-\\w\u2013.,\xad])\\b[\u041d\u043d][\u0418\u0438][\u041a\u043a][\u0422\u0442][\u041e\u043e] [\u0418\u0438][\u041d\u043d][\u041e\u043e][\u0419\u0439], [\u041d\u043d][\u0415\u0435]\\b(?![-\\w\u2013\xad])', u'\u043d\u0438\u043a\u0442\u043e \u0438\u043d\u043e\u0439 \u043d\u0435', u'\u041e\u0431\u043e\u0440\u043e\u0442.', u'option(LOCALE,"multiword")'], [u'(?iu)(?<![-\\w\u2013.,\xad])\\b[\u041d\u043d][\u0418\u0438][\u0427\u0447][\u0422\u0442][\u041e\u043e] [\u0418\u0438][\u041d\u043d][\u041e\u043e][\u0415\u0435], [\u041d\u043d][\u0415\u0435]\\b(?![-\\w\u2013\xad])', u'\u043d\u0438\u0447\u0442\u043e \u0438\u043d\u043e\u0435 \u043d\u0435', u'\u041e\u0431\u043e\u0440\u043e\u0442.', u'option(LOCALE,"multiword")'], [u'(?iu)(?<![-\\w\u2013.,\xad])\\b[\u041d\u043d][\u0418\u0438] [\u041a\u043a][\u0422\u0442][\u041e\u043e] [\u0418\u0438][\u041d\u043d][\u041e\u043e][\u0419\u0439], [\u041d\u043d][\u0415\u0435]\\b(?![-\\w\u2013\xad])', u'\u043d\u0438\u043a\u0442\u043e \u0438\u043d\u043e\u0439 \u043d\u0435', u'\u041e\u0431\u043e\u0440\u043e\u0442.', u'option(LOCALE,"multiword")'], [u'(?iu)(?<![-\\w\u2013.,\xad])\\b[\u041d\u043d][\u0418\u0438] [\u0427\u0447][\u0422\u0442][\u041e\u043e] [\u0418\u0438][\u041d\u043d][\u041e\u043e][\u0415\u0435], [\u041d\u043d][\u0415\u0435]\\b(?![-\\w\u2013\xad])', u'\u043d\u0438\u0447\u0442\u043e \u0438\u043d\u043e\u0435 \u043d\u0435', u'\u041e\u0431\u043e\u0440\u043e\u0442.', u'option(LOCALE,"multiword")'], [u'(?iu)(?<![-\\w\u2013.,\xad])\\b[\u041a\u043a][\u0410\u0430][\u041a\u043a][\u0411\u0431][\u0423\u0443][\u0414\u0434][\u0422\u0442][\u041e\u043e](?![-\\w\u2013\xad])', u'\u043a\u0430\u043a \u0431\u0443\u0434\u0442\u043e', u'\u0421\u043e\u0441\u0442\u0430\u0432\u043d\u0430\u044f \u0447\u0430\u0441\u0442\u0438\u0446\u0430', u'option(LOCALE,"together")'], [u'(?iu)(?<![-\\w\u2013.,\xad])\\b[\u041f\u043f][\u041e\u043e] [\u041c\u043c][\u0418\u0438][\u041c\u043c][\u041e\u043e]\\b(?![-\\w\u2013\xad])', u'\u043f\u043e\u043c\u0438\u043c\u043e', u'\u041f\u0438\u0448\u0435\u0442\u0441\u044f \u0441\u043b\u0438\u0442\u043d\u043e', u'option(LOCALE,"together")'], [u'(?iu)(?<![-\\w\u2013.,\xad])\\b[\u041d\u043d][\u0410\u0430] [\u041a\u043a][\u0410\u0430][\u041d\u043d][\u0423\u0443][\u041d\u043d][\u0415\u0435]\\b(?![-\\w\u2013\xad])', u'\u043d\u0430\u043a\u0430\u043d\u0443\u043d\u0435', u'\u0421\u043b\u0438\u0442\u043d\u043e', u'option(LOCALE,"together")'], [u'(?iu)(?<![-\\w\u2013.,\xad])\\b[\u041d\u043d][\u0410\u0430] [\u041f\u043f][\u041e\u043e][\u0414\u0434][\u041e\u043e][\u0411\u0431][\u0418\u0438][\u0415\u0435]\\b(?![-\\w\u2013\xad])', u'\u043d\u0430\u043f\u043e\u0434\u043e\u0431\u0438\u0435', u'\u0421\u043b\u0438\u0442\u043d\u043e', u'option(LOCALE,"together")'], [u'(?iu)(?<![-\\w\u2013.,\xad])\\b[\u041d\u043d][\u0410\u0430] [\u041f\u043f][\u0420\u0440][\u041e\u043e][\u0422\u0442][\u0418\u0438][\u0412\u0432]\\b(?![-\\w\u2013\xad])', u'\u043d\u0430\u043f\u0440\u043e\u0442\u0438\u0432', u'\u0421\u043b\u0438\u0442\u043d\u043e', u'option(LOCALE,"together")'], [u'(?iu)(?<![-\\w\u2013.,\xad])\\b[\u0412\u0432] [\u041d\u043d][\u0418\u0438][\u0417\u0437][\u0423\u0443]\\b(?![-\\w\u2013\xad])', u'\u0432\u043d\u0438\u0437\u0443', u'\u0421\u043b\u0438\u0442\u043d\u043e', u'option(LOCALE,"together")'], [u'(?iu)(?<![-\\w\u2013.,\xad])\\b[\u0421\u0441] [\u041d\u043d][\u0418\u0438][\u0417\u0437][\u0423\u0443]\\b(?![-\\w\u2013\xad])', u'\u0441\u043d\u0438\u0437\u0443', u'\u0421\u043b\u0438\u0442\u043d\u043e', u'option(LOCALE,"together")'], [u'(?iu)(?<![-\\w\u2013.,\xad])\\b[\u041d\u043d][\u0410\u0430] [\u0412\u0432][\u0415\u0435][\u0420\u0440][\u0425\u0445][\u0423\u0443]\\b(?![-\\w\u2013\xad])', u'\u043d\u0430\u0432\u0435\u0440\u0445\u0443', u'\u0421\u043b\u0438\u0442\u043d\u043e', u'option(LOCALE,"together")'], [u'(?iu)(?<![-\\w\u2013.,\xad])\\b[\u0412\u0432] [\u0412\u0432][\u0415\u0435][\u0420\u0440][\u0425\u0445][\u0423\u0443]\\b(?![-\\w\u2013\xad])', u'\u0432\u0432\u0435\u0440\u0445\u0443', u'\u0421\u043b\u0438\u0442\u043d\u043e', u'option(LOCALE,"together")'], [u'(?iu)(?<![-\\w\u2013.,\xad])\\b[\u0421\u0441] [\u0412\u0432][\u0415\u0435][\u0420\u0440][\u0425\u0445][\u0423\u0443]\\b(?![-\\w\u2013\xad])', u'\u0441\u0432\u0435\u0440\u0445\u0443', u'\u0421\u043b\u0438\u0442\u043d\u043e', u'option(LOCALE,"together")'], [u'(?iu)(?<![-\\w\u2013.,\xad])\\b[\u0421\u0441] [\u0412\u0432][\u0415\u0435][\u0420\u0440][\u0425\u0445]\\b(?![-\\w\u2013\xad])', u'\u0441\u0432\u0435\u0440\u0445', u'\u0421\u043b\u0438\u0442\u043d\u043e', u'option(LOCALE,"together")'], [u'(?iu)(?<![-\\w\u2013.,\xad])\\b[\u0421\u0441] [\u0412\u0432][\u042b\u044b][\u0428\u0448][\u0415\u0435]\\b(?![-\\w\u2013\xad])', u'\u0441\u0432\u044b\u0448\u0435', u'\u0421\u043b\u0438\u0442\u043d\u043e', u'option(LOCALE,"together")'], [u'(?iu)(?<![-\\w\u2013.,\xad])\\b[\u0421\u0441][\u041e\u043e] [\u0413\u0433][\u041b\u043b][\u0410\u0430][\u0421\u0441][\u041d\u043d][\u041e\u043e]\\b(?![-\\w\u2013\xad])', u'\u0441\u043e\u0433\u043b\u0430\u0441\u043d\u043e', u'\u0421\u043b\u0438\u0442\u043d\u043e', u'option(LOCALE,"together")'], [u'(?iu)(?<![-\\w\u2013.,\xad])\\b[\u0412\u0432] [\u0413\u0433][\u041b\u043b][\u0423\u0443][\u0411\u0431][\u042c\u044c]\\b(?![-\\w\u2013\xad])', u'\u0432\u0433\u043b\u0443\u0431\u044c', u'\u0421\u043b\u0438\u0442\u043d\u043e', u'option(LOCALE,"together")'], [u'(?iu)(?<![-\\w\u2013.,\xad])\\b[\u0412\u0432] [\u0414\u0434][\u041e\u043e][\u041b\u043b][\u042c\u044c]\\b(?![-\\w\u2013\xad])', u'\u0432\u0434\u043e\u043b\u044c', u'\u0421\u043b\u0438\u0442\u043d\u043e', u'option(LOCALE,"together")'], [u'(?iu)(?<![-\\w\u2013.,\xad])\\b[\u0412\u0432] [\u0417\u0437][\u0410\u0430][\u041c\u043c][\u0415\u0435][\u041d\u043d]\\b(?![-\\w\u2013\xad])', u'\u0432\u0437\u0430\u043c\u0435\u043d', u'\u0421\u043b\u0438\u0442\u043d\u043e', u'option(LOCALE,"together")'], [u'(?iu)(?<![-\\w\u2013.,\xad])\\b(?P<d2_1>\\d\\d)(?P<d_1>\\d\\d\\d)\\b(?![-\\w\u2013\xad])', u'\\g<d2_1>\xa0\\g<d_1>', u'\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0440\u0430\u0437\u0434\u0435\u043b\u0438\u0442\u0435\u043b\u044c \u0440\u0430\u0437\u0440\u044f\u0434\u043e\u0432 (ISO)?', u'option(LOCALE,"numsep")'], [u'(?iu)(?<![-\\w\u2013.,\xad])\\b(?P<D_1>\\d|\\d\\d|\\d\\d\\d)(?P<d_1>\\d\\d\\d)(?P<d_2>\\d\\d\\d)\\b(?![-\\w\u2013\xad])', u'\\g<D_1>\xa0\\g<d_1>\xa0\\g<d_2>', u'\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0440\u0430\u0437\u0434\u0435\u043b\u0438\u0442\u0435\u043b\u044c \u0440\u0430\u0437\u0440\u044f\u0434\u043e\u0432 (ISO)?', u'option(LOCALE,"numsep")'], [u'(?iu)(?<![-\\w\u2013.,\xad])\\b(?P<D_1>\\d|\\d\\d|\\d\\d\\d)(?P<d_1>\\d\\d\\d)(?P<d_2>\\d\\d\\d)(?P<d_3>\\d\\d\\d)\\b(?![-\\w\u2013\xad])', u'\\g<D_1>\xa0\\g<d_1>\xa0\\g<d_2>\xa0\\g<d_3>', u'\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0440\u0430\u0437\u0434\u0435\u043b\u0438\u0442\u0435\u043b\u044c \u0440\u0430\u0437\u0440\u044f\u0434\u043e\u0432 (ISO)?', u'option(LOCALE,"numsep")'], [u'(?iu)(?<![-\\w\u2013.,\xad])(?P<W_1>[-\\w]{3,})(?: [-\u2013\\w\u201c\u201d]+)* \\1(?![-\\w\u2013\xad])', u'\\g<W_1>', u'\u041f\u043e\u0432\u0442\u043e\u0440 \u0441\u043b\u043e\u0432\u0430?', u'option(LOCALE,"dup")'], [u'(?iu)(?<![-\\w\u2013.,\xad])(?P<W_1>[-\\w]{3,})[;,:]?(?: [-\u2013\\w\u201c\u201d]+[;,:]?)* \\1(?![-\\w\u2013\xad])', u'\\g<W_1>', u'\u041f\u043e\u0432\u0442\u043e\u0440 \u0441\u043b\u043e\u0432\u0430?', u'option(LOCALE,"dup2")']]
