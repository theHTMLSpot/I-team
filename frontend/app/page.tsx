import Hero from "./components/hero";
import styles from "./page.module.css";


export default function Home() {
  return (
    <main className={styles.main}>
     <Hero/>
    </main>
  );
}
