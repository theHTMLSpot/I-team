import Image from 'next/image';
import styles from '../page.module.css';

function Hero() {
  return (
    <div className={styles.hero}>
      <div className={styles.left}>
        <h1 className={styles.title}>
        Welkom bij I-Team: Innovatie en Technologie op School
        </h1>
        <p className={styles.description}>
        Bij I-Team richten we ons op innovatieve technologieën en vooruitgang. Ons expertteam lost uitdagende problemen op en creëert nieuwe mogelijkheden, van softwareontwikkeling tot strategisch advies. Ontdek hoe wij de toekomst vormgeven met onze oplossingen. </p>
        <button className={styles.cta}>
          Join Nu!
        </button>
      </div>
      <div className={styles.right}>
        <Image src="/i-team.jpeg" alt="I-Team" layout="responsive" width={200} height={200} className={styles.image}/>
      </div>
    </div>
  );
}

export default Hero;