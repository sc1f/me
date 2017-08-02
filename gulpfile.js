var gulp = require('gulp'),
    sass = require('gulp-sass'),
    basedir = './static/css';

gulp.task('sass', function () {

    gulp.src(basedir + 'main.scss')

        .pipe(sass())

        .pipe(gulp.dest(basedir));

});


gulp.task('foundation_sass', function () {

    gulp.src(basedir + 'custom_foundation.scss')

        .pipe(sass())

        .pipe(gulp.dest(basedir));

});

gulp.task('watch', function() {
    gulp.watch(basedir + 'imports/*.scss', ['sass']);
    gulp.watch(basedir + 'main.scss', ['sass']);
    gulp.watch(basedir + 'tejascustomfoundation.scss', ['foundation_sass'])

});

gulp.task('default', ['sass', 'foundation_sass', 'watch']);