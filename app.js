const express = require('express');

const app = express();
app.listen(3000);
app.set('view engine', 'ejs');
app.use(express.static('public'));
app.use(express.urlencoded({ extended: true }))

const TITLE = '| EFTUN.net - Türkiye\'nin alışveriş platformu!'

console.log('EFTUN Hazır!');

app.get('/', (req, res) => {
    res.render('index', {title: `Anasayfa ${TITLE}`});
});

app.post('/', (req, res) => {
    let search = req.body.search;
    search = String(search);

    if (search.length > 1) {
        res.redirect('/arama/' + search);
    } else {
        res.redirect('/');
    }
});

app.get('/urunler', (req, res) => {
    res.render('product', { title: `Ürünler ${TITLE}` });
});